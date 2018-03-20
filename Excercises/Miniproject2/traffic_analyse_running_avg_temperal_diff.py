import numpy as np
import cv2
import sys

# cap = cv2.VideoCapture('2017_06_23_1430_Falen_Cigaren_mod_byen.mp4')
cap = cv2.VideoCapture('2015_06_27_1630_Krydset_Motorvejsafkørsel_52.mp4') # 35 / 6 / 2
# cap = cv2.VideoCapture('KrydsetFaaborgvejSanderumvej1.mp4')

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.namedWindow("avg", cv2.WINDOW_NORMAL)
cv2.namedWindow("TD", cv2.WINDOW_NORMAL)
cv2.namedWindow("TD_thres", cv2.WINDOW_NORMAL)
cv2.namedWindow("avg_thres", cv2.WINDOW_NORMAL)
cv2.namedWindow("avg_frame", cv2.WINDOW_NORMAL)

def nothing(x):
    pass

cv2.createTrackbar('threshold_TD','frame',0,255, nothing)
cv2.createTrackbar('threshold_AVG','frame',0,255, nothing)
cv2.createTrackbar('alpha','frame',0,100, nothing)
cv2.createTrackbar('opening','frame',1,100, nothing)
cv2.createTrackbar('closing','frame',1,100, nothing)

# Init pos
cv2.setTrackbarPos('threshold_TD', 'frame', 0) #38
cv2.setTrackbarPos('threshold_AVG', 'frame', 0) #38
cv2.setTrackbarPos('alpha', 'frame', 1)
cv2.setTrackbarPos('opening', 'frame', 1)
cv2.setTrackbarPos('closing', 'frame', 1)

### Params ###
stabilize = False

### init Fast for image stabilization ###
orb = cv2.ORB_create()
MIN_MATCH_COUNT = 10

# FLANN parameters
FLANN_INDEX_LSH = 6
index_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6, # 12
                   key_size = 12,     # 20
                   multi_probe_level = 1) #2
search_params = dict(checks=50)   # or pass empty dictionary

flann = cv2.FlannBasedMatcher(index_params, search_params)

# initlize
ret, firstFrame = cap.read()
firstFrame = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
avg = np.float32(firstFrame)

prevFrame = firstFrame

while cap.isOpened():
    ret, currFrame = cap.read()

    outFrame = currFrame
    currFrame = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)

    # trackbars
    thrs_td = cv2.getTrackbarPos('threshold_TD', 'frame')
    thrs_avg = cv2.getTrackbarPos('threshold_AVG', 'frame')
    alpha = cv2.getTrackbarPos('alpha', 'frame')
    kernel_open = cv2.getTrackbarPos('opening','frame')
    kernel_close = cv2.getTrackbarPos('closing','frame')

    # Stabilize image #
    if stabilize:
        greyFrame = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)
        currKP, currDes = orb.detectAndCompute(greyFrame, None)
        # currKP, currDes = fast.detectAndCompute(greyFrame, None)

        #Match
        matches = flann.knnMatch(refDes, currDes, k=2)
        # Apply ratio test
        good = []
        for m_n in matches:
            if len(m_n) != 2:
                continue
            (m, n) = m_n
            if m.distance < 0.75 * n.distance:
                good.append(m)

        print(len(good))

        # perspective change
        if len(good) > MIN_MATCH_COUNT:

            src_pts = np.float32([refKP[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            dst_pts = np.float32([currKP[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            matchesMask = mask.ravel().tolist()

            h, w, depth = currFrame.shape
            currFrame = cv2.warpPerspective(currFrame, M, (w, h))

            # #TODO debug drawing FAST features
            # pts = np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
            # dst = cv2.perspectiveTransform(pts, M)
            # flowFrame = cv2.polylines(currFrame, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
        else:
            print("Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT))
            matchesMask = None

    # blurFrame = cv2.blur(currFrame, (5, 5))

    # Running Average #
    # Implement running average and get mask from background
    cv2.accumulateWeighted(currFrame, avg, alpha/100)
    running_res = cv2.convertScaleAbs(avg)
    avg_frame = running_res

    # Subtract this from current frame to get moving parts?
    running_res = cv2.absdiff(currFrame, running_res)
    _, running_res_thres = cv2.threshold(running_res, thrs_avg, 255, cv2.THRESH_BINARY_INV)


    # Temperal difference #
    # Implement temperal difference and get mask
    diff_frame = cv2.absdiff(currFrame, prevFrame)
    _, diff_frame_thres = cv2.threshold(diff_frame, thrs_td, 255, cv2.THRESH_BINARY)

    # Logic AND masks together #
    moving_objs = cv2.bitwise_and(running_res, diff_frame)
    bg_subtracted = cv2.bitwise_and(currFrame, currFrame, mask=diff_frame)

    # Morphology to remove noise #
    kernel_open = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_open,kernel_open))
    kernel_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_close,kernel_close))

    morphImg = cv2.morphologyEx(moving_objs, cv2.MORPH_OPEN, kernel_open)
    morphImg = cv2.morphologyEx(morphImg, cv2.MORPH_CLOSE, kernel_close)

    # Connected components to get moving objects #

    # # You need to choose 4 or 8 for connectivity type
    # connectivity = 4
    # # Perform the operation
    # output = cv2.connectedComponentsWithStats(morphImg, connectivity, cv2.CV_32S)
    # # Get the results
    # # The first cell is the number of labels
    # num_labels = output[0]
    # # The second cell is the label matrix
    # labels = output[1]
    # # The third cell is the stat matrix
    # stats = output[2]
    # # The fourth cell is the centroid matrix
    # centroids = output[3]
    #
    # for i in range(0, len(centroids)):
    #     top = stats[i, cv2.CC_STAT_TOP]
    #     left = stats[i, cv2.CC_STAT_LEFT]
    #     width = stats[i, cv2.CC_STAT_WIDTH]
    #     height = stats[i, cv2.CC_STAT_HEIGHT]
    #
    #     if stats[i, cv2.CC_STAT_AREA] < cc_min: continue
    #
    #     cv2.rectangle(outFrame, (left, top), (left + width, top + height), (0, 0, 255), 2)
    #     cv2.rectangle(morphImg, (left, top), (left + width, top + height), (0, 0, 255), 2)
    #
    #     # cv2.putText(currFrame, 'Car Detected', (left + width + 10, top + height), 0, 0.3, (0, 0, 255))

    prevFrame = currFrame

    cv2.imshow('frame', morphImg)
    cv2.imshow('avg', running_res)
    cv2.imshow('TD', diff_frame)
    cv2.imshow('TD_thres', diff_frame_thres)
    cv2.imshow('avg_thres', running_res_thres)
    cv2.imshow('avg_frame', avg_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
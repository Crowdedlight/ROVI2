import numpy as np
import cv2
import sys


def GetMaskFromAnnotated(annotated):

    #rgbAnnotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

    bgrMin = np.array([0, 0, 255])
    bgrMax = np.array([0, 0, 255])

    maskRGB = cv2.inRange(annotated, bgrMin, bgrMax)
    return maskRGB


# cap = cv2.VideoCapture('2017_06_23_1430_Falen_Cigaren_mod_byen.mp4')
cap = cv2.VideoCapture('2015_06_27_1630_Krydset_Motorvejsafkørsel_52.mp4') # 35 / 6 / 2
# cap = cv2.VideoCapture('KrydsetFaaborgvejSanderumvej1.mp4')

prevFrame = None
currFrame = None

# annotated = cv2.imread("motorvej52_annotated_red.png", cv2.IMREAD_COLOR)
# annotatedMask = GetMaskFromAnnotated(annotated)

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False, history=50, varThreshold=30)

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.namedWindow("unprocessed_frame", cv2.WINDOW_NORMAL)
# cv2.namedWindow("Optical_Flow", cv2.WINDOW_NORMAL)

def nothing(x):
    pass

cv2.createTrackbar('cc_min','frame',0,3000, nothing)
cv2.createTrackbar('max_area','frame',0,3000, nothing)
cv2.createTrackbar('opening','frame',1,100, nothing)
cv2.createTrackbar('closing','frame',1,100, nothing)

# Init pos
cv2.setTrackbarPos('cc_min', 'frame', 35)
cv2.setTrackbarPos('opening', 'frame', 6)
cv2.setTrackbarPos('closing', 'frame', 2)

### init Fast for image stabilization ###
# Initiate FAST object with default values
# fast = cv2.FastFeatureDetector_create(nonmaxSuppression=False)
# orb = cv2.ORB_create()
# MIN_MATCH_COUNT = 10
#
# # FLANN parameters
# FLANN_INDEX_LSH = 6
# index_params= dict(algorithm = FLANN_INDEX_LSH,
#                    table_number = 6, # 12
#                    key_size = 12,     # 20
#                    multi_probe_level = 1) #2
# search_params = dict(checks=100)   # or pass empty dictionary

# For FAST
# FLANN_INDEX_KDTREE = 0
# index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
# search_params = dict(checks=50)

# flann = cv2.FlannBasedMatcher(index_params, search_params)

# Init optical flow
# params for ShiTomasi corner detection
# feature_params = dict( maxCorners = 100,
#                        qualityLevel = 0.3,
#                        minDistance = 7,
#                        blockSize = 7 )
# # Parameters for lucas kanade optical flow
# lk_params = dict(winSize=(15, 15),
#                  maxLevel=2,
#                  criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
# # Create some random colors
# color = np.random.randint(0, 255, (100, 3))

# initlize
# ret, firstFrame = cap.read()
# firstFrame = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
# refKP, refDes = orb.detectAndCompute(firstFrame, None)
# refKP, refDes = fast.detectAndCompute(firstFrame, None)

while cap.isOpened():
    ret, currFrame = cap.read()

    outFrame = currFrame
    # flowFrame = currFrame
    # currFrame = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)

    # trackbars
    cc_min = cv2.getTrackbarPos('cc_min','frame')
    kernel_open = cv2.getTrackbarPos('opening','frame')
    kernel_close = cv2.getTrackbarPos('closing','frame')

    # only keep stuff inside mask from annotation - TODO Do not use annotation, as we want it to work all places
    # currFrame_mask = cv2.bitwise_and(currFrame, currFrame, mask=annotatedMask)

    # Stabilize image
    greyFrame = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)
    # currKP, currDes = orb.detectAndCompute(greyFrame, None)
    # # currKP, currDes = fast.detectAndCompute(greyFrame, None)
    #
    # #Match
    # matches = flann.knnMatch(refDes, currDes, k=2)
    # # Apply ratio test
    # good = []
    # for m_n in matches:
    #     if len(m_n) != 2:
    #         continue
    #     (m, n) = m_n
    #     if m.distance < 0.75 * n.distance:
    #         good.append(m)
    #
    # # perspective change
    # if len(good) > MIN_MATCH_COUNT:
    #
    #     src_pts = np.float32([refKP[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    #     dst_pts = np.float32([currKP[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    #
    #     M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    #     matchesMask = mask.ravel().tolist()
    #
    #     h, w, depth = currFrame.shape
    #     currFrame = cv2.warpPerspective(currFrame, M, (w, h))
    #
    #     #TODO debug drawing FAST features
    #     pts = np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    #     dst = cv2.perspectiveTransform(pts, M)
    #     flowFrame = cv2.polylines(currFrame, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
    # else:
    #     print("Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT))
    #     matchesMask = None

    # kp = np.array([idx.pt for idx in kp])
    # print(len(kp))
    # print(len(prevKP))
    # estMotion = cv2.estimateRigidTransform(firstFrame, currFrame, fullAffine=False)
    # print(estMotion)
    # flowFrame = cv2.warpAffine(currFrame, estMotion, currFrame.size())
    # h = cv2.findHomography(prevKP, kp)
    # flowFrame = cv2.warpPerspective(currFrame, h, currFrame.size())

    # blurFrame = cv2.blur(currFrame_mask, (5, 5))
    blurFrame = cv2.blur(currFrame, (5, 5))

    fgmask = fgbg.apply(blurFrame)

    kernel_open = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_open,kernel_open))
    kernel_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_close,kernel_close))
    morphImg = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel_open)
    morphImg = cv2.morphologyEx(morphImg, cv2.MORPH_CLOSE, kernel_close)

    # You need to choose 4 or 8 for connectivity type
    connectivity = 4
    # Perform the operation
    output = cv2.connectedComponentsWithStats(morphImg, connectivity, cv2.CV_32S)
    # Get the results
    # The first cell is the number of labels
    num_labels = output[0]
    # The second cell is the label matrix
    labels = output[1]
    # The third cell is the stat matrix
    stats = output[2]
    # The fourth cell is the centroid matrix
    centroids = output[3]

    for i in range(0, len(centroids)):
        top = stats[i, cv2.CC_STAT_TOP]
        left = stats[i, cv2.CC_STAT_LEFT]
        width = stats[i, cv2.CC_STAT_WIDTH]
        height = stats[i, cv2.CC_STAT_HEIGHT]

        if stats[i, cv2.CC_STAT_AREA] < cc_min: continue

        cv2.rectangle(outFrame, (left, top), (left + width, top + height), (0, 0, 255), 2)
        cv2.rectangle(morphImg, (left, top), (left + width, top + height), (0, 0, 255), 2)

        # cv2.putText(currFrame, 'Car Detected', (left + width + 10, top + height), 0, 0.3, (0, 0, 255))

        # if init is True:
        #     # p0 = (top, left, width, height)
        #     p0 = cv2.goodFeaturesToTrack(prevFrame, mask=None, **feature_params)
        #
        #     # calculate optical flow
        #     p1, st, err = cv2.calcOpticalFlowPyrLK(prevFrame, morphImg, p0, None, **lk_params)
        #     # Select good points
        #     good_new = p1[st == 1]
        #     good_old = p0[st == 1]
        #
        #     # draw the tracks
        #     for i, (new, old) in enumerate(zip(good_new, good_old)):
        #         a, b = new.ravel()
        #         c, d = old.ravel()
        #         mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
        #         frame = cv2.circle(morphImg, (a, b), 5, color[i].tolist(), -1)
        #         flowFrame = cv2.add(frame, mask)
        #
        #     # set last used image
        #     prevFrame = morphImg.copy()
        #     p0 = good_new.reshape(-1, 1, 2)
        #
        # else: init = False

    cv2.imshow('frame', morphImg)
    cv2.imshow('unprocessed_frame', outFrame)
    # cv2.imshow('Optical_Flow', flowFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
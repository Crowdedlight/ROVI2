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

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.namedWindow("unprocessed_frame", cv2.WINDOW_NORMAL)
cv2.namedWindow("Optical_Flow", cv2.WINDOW_NORMAL)

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

# Init optical flow
# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )
# Parameters for lucas kanade optical flow
lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
# Create some random colors
color = np.random.randint(0, 255, (100, 3))

#initlize
init = False

while cap.isOpened():
    ret, currFrame = cap.read()

    outFrame = currFrame
    flowFrame = currFrame
    # currFrame = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)

    # trackbars
    cc_min = cv2.getTrackbarPos('cc_min','frame')
    kernel_open = cv2.getTrackbarPos('opening','frame')
    kernel_close = cv2.getTrackbarPos('closing','frame')

    # only keep stuff inside mask from annotation
    # currFrame_mask = cv2.bitwise_and(currFrame, currFrame, mask=annotatedMask)

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

        if init is True:
            # p0 = (top, left, width, height)
            p0 = cv2.goodFeaturesToTrack(prevFrame, mask=None, **feature_params)

            # calculate optical flow
            p1, st, err = cv2.calcOpticalFlowPyrLK(prevFrame, morphImg, p0, None, **lk_params)
            # Select good points
            good_new = p1[st == 1]
            good_old = p0[st == 1]

            # draw the tracks
            for i, (new, old) in enumerate(zip(good_new, good_old)):
                a, b = new.ravel()
                c, d = old.ravel()
                mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
                frame = cv2.circle(morphImg, (a, b), 5, color[i].tolist(), -1)
                flowFrame = cv2.add(frame, mask)

            # set last used image
            prevFrame = morphImg.copy()
            p0 = good_new.reshape(-1, 1, 2)

        else: init = False

    cv2.imshow('frame', morphImg)
    cv2.imshow('unprocessed_frame', outFrame)
    # cv2.imshow('Optical_Flow', flowFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
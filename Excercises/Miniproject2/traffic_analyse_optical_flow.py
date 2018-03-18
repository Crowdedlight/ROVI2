import numpy as np
import cv2
import sys

cap = cv2.VideoCapture('2015_06_27_1630_Krydset_Motorvejsafkørsel_52.mp4') # 35 / 6 / 2

currFrame = None

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.namedWindow("background_sub", cv2.WINDOW_NORMAL)
cv2.namedWindow("Optical_Flow", cv2.WINDOW_NORMAL)

def nothing(x):
    pass


cv2.createTrackbar('opening','frame',1,100, nothing)
cv2.createTrackbar('closing','frame',1,100, nothing)

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)


# Init pos
cv2.setTrackbarPos('opening', 'frame', 6)
cv2.setTrackbarPos('closing', 'frame', 2)

# Init optical flow
init = False
prevGray = None
p0 = np.array([])
p1 = np.array([])
good_old = np.array([])
good_new = np.array([])
update_count = 0
# params for ShiTomasi corner detection
feature_params = dict( maxCorners=100,
                       qualityLevel=0.5,
                       minDistance=7,
                       blockSize=7)
# Parameters for lucas kanade optical flow
lk_params = dict(winSize=(15, 15),
                 maxLevel=1,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.05))
# Create some random colors
color = np.random.randint(0, 255, (100, 3))

while cap.isOpened():
    ret, currFrame = cap.read()

    currGray = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)
    outFrame = currFrame
    flowFrame = currFrame
    mask_flow = currGray.copy()

    # Trackbars
    kernel_open = cv2.getTrackbarPos('opening','frame')
    kernel_close = cv2.getTrackbarPos('closing','frame')

    # updater
    update_count += 1

    # Background substraction
    blurFrame = cv2.blur(currFrame, (5, 5))
    fgmask = fgbg.apply(blurFrame)

    kernel_open = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_open, kernel_open))
    kernel_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_close, kernel_close))
    morphImg = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel_open)
    morphImg = cv2.morphologyEx(morphImg, cv2.MORPH_CLOSE, kernel_close)

    # If init do optical flow based on mask from background sub, otherwise init
    if init:
        # calculate optical flow
        p1, st, err = cv2.calcOpticalFlowPyrLK(prevGray, currGray, p0, None, **lk_params)
        # Select good points
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        # update every 5 frames
        if update_count >= 5:
            mask_flow[:] = 255
            mask_flow = cv2.subtract(mask_flow, morphImg)
            p0 = cv2.goodFeaturesToTrack(currGray, mask=mask_flow, **feature_params)
            update_count = 0
            cv2.imshow('background_sub', mask_flow)

        # draw the tracks
        mask = None
        frame = None
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            mask = cv2.line(currFrame, (a, b), (c, d), color[i].tolist(), 2)
            frame = cv2.circle(currFrame, (a, b), 5, color[i].tolist(), -1)

        # update last points from new points
        p0 = good_new.reshape(-1, 1, 2)

    else:
        # Init Frame
        p0 = cv2.goodFeaturesToTrack(currGray, mask=None, **feature_params)
        init = True

    # set last used image
    prevGray = currGray.copy()

    cv2.imshow('frame', currFrame)
    # cv2.imshow('background_sub', mask_flow)
    cv2.imshow('Optical_Flow', flowFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
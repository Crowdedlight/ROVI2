import numpy as np
import cv2
from numpy.linalg import inv, norm
from scipy.spatial import distance
from kalman import KalmanFilter

#empty passer for trackbars
def nothing(x):
    pass


def backgroundSubtraction(frame):
    kernel_open = cv2.getTrackbarPos('opening', 'frame')
    kernel_close = cv2.getTrackbarPos('closing', 'frame')

    blurFrame = cv2.blur(frame, (6, 6))  # 10,10

    fgmask = fgbg.apply(blurFrame)

    kernel_open = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_open, kernel_open))
    kernel_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_close, kernel_close))
    morphImg = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel_open)
    morphImg = cv2.morphologyEx(morphImg, cv2.MORPH_CLOSE, kernel_close)

    return morphImg


def connectedComponents(frame):
    # You need to choose 4 or 8 for connectivity type
    connectivity = 4
    # Perform the operation
    output = cv2.connectedComponentsWithStats(frame, connectivity, cv2.CV_32S)
    # Get the results
    # The first cell is the number of labels
    num_labels = output[0]
    # The second cell is the label matrix
    labels = output[1]
    # The third cell is the stat matrix
    stats = output[2]
    # The fourth cell is the centroid matrix
    centroids = output[3]

    return stats, centroids


def thresholdComponents(stats, centroids):
    thresComponent = []

    for i in range(0, len(centroids)):
        t = stats[i, cv2.CC_STAT_TOP]
        l = stats[i, cv2.CC_STAT_LEFT]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]

        if stats[i, cv2.CC_STAT_AREA] < cc_min or stats[i, cv2.CC_STAT_AREA] > 10000: continue

        thresComponent.append((l, t, w, h, 0)) # todo ugly hack, 0 = velocity. Needed for using same homography function

    return thresComponent


def doHomography(inputVector, H):

    changedVector = []

    oldPoints = np.array([[[elem[0], elem[1]]] for elem in inputVector], dtype='float32')

    newPoints = cv2.perspectiveTransform(oldPoints, H)

    for i, elem in enumerate(newPoints):
        changedVector.append([elem[0,0], elem[0,1], inputVector[i][2], inputVector[i][3], inputVector[i][4]])

    return changedVector


# find best component for current kalman filter
def nearestNeighbour(k_pos, components):
    components = np.asarray([[i[0],i[1]] for i in components])

    dists = distance.cdist([k_pos], components)

    closest_idx = dists[0].argmin()

    return closest_idx, dists[0][closest_idx]


def pixVel2realVel(pixVel,mPerPix):
    # Calculate the velocity in km/h from pixel/s

    v_real = mPerPix*pixVel*3.6

    return v_real

def realVel2PixelVel(realVel,mPerPix):
    # Calculate the velocity in km/h from pixel/s

    v_pixel = realVel/(mPerPix*3.6)

    return v_pixel


## Windows & Trackbars
cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.namedWindow("unprocessed_frame", cv2.WINDOW_NORMAL)

cv2.createTrackbar('cc_min','frame',0,3000, nothing)
cv2.createTrackbar('max_area','frame',0,3000, nothing)
cv2.createTrackbar('opening','frame',1,100, nothing)
cv2.createTrackbar('closing','frame',1,100, nothing)

# Init pos
cv2.setTrackbarPos('cc_min', 'frame', 38) #38
cv2.setTrackbarPos('opening', 'frame', 3) #
cv2.setTrackbarPos('closing', 'frame', 4) #

### Params ###
cap = cv2.VideoCapture('2015_06_27_1630_Krydset_Motorvejsafkørsel_52.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False, history=50, varThreshold=30)
k_filters = []
trajectories = []
nearestNeighbourThreshold = 35

# Homography to take perspective into account #
old_corners = np.array([[450, 235], [1385, 312], [1362, 928], [396, 711]])
new_corners = np.array([[846, 20], [639, 573], [266, 442], [361, 178]]) * 1

H, _ = cv2.findHomography(old_corners, new_corners)
invH = inv(H)

# Pixel distance
a = np.array([new_corners[0,0],new_corners[0,1]])
b = np.array([new_corners[1,0],new_corners[1,1]])
d = norm(b - a)

# Measured distance
meas_d = 400 # [meters]

meterPerPixel = meas_d / d

# Kalman filter thresholds
# Velocity threshold
v_thresh = realVel2PixelVel(10, meterPerPixel)
# Max predictions
max_predictions = 80
# Amount of corrections before kf is valid
corrections = 20

H, _ = cv2.findHomography(old_corners, new_corners)
invH = inv(H)

while cap.isOpened():
    ret, currFrame = cap.read()

    #output frame
    outFrame = currFrame

    # get foreground from background Subtraction
    foregroundFrame = backgroundSubtraction(currFrame)

    # Connected components on our foreground
    stats, centroids = connectedComponents(foregroundFrame)

    # Get threshold
    cc_min = cv2.getTrackbarPos('cc_min', 'frame')

    # corrections
    components = thresholdComponents(stats, centroids)

    if len(components) != 0:
        homografed = doHomography(components, H)

        # nearest neighbour
        for k in k_filters:

            # if we reach zero components before filling all kalman filters, update rest kalman filters with no points
            if len(homografed) <= 0:
                k.update()
                continue

            # get nearest component
            index, dist = nearestNeighbour(k.getPosition(), homografed)
            # if component is too far away, skip this array ==> continue
            if dist > nearestNeighbourThreshold:
                k.update()
            else:
                x_c = homografed[index][0]
                y_c = homografed[index][1]
                k.update(np.array([[x_c], [y_c]]))

                # remove component from components list and keep going
                del homografed[index]

            # todo, if it haven't received corrections for some time, kill filter


        # For remainders in components that do not have a friend in k
        for c in homografed:
            # make new kalman filter
            state = np.array([[c[0]], [c[1]], [0], [0]])
            fps = cap.get(cv2.CAP_PROP_FPS)
            # state, fps, boxWidth, box Height

            k_filters.append(KalmanFilter(state, 1.0/fps, c[2], c[3], max_predictions, v_thresh, corrections))

    else:
        # no detections, just update kalman filters
        for k in k_filters:
            k.update()

    # Get output from kalman and change to original homography
    homoList = []
    indexList = []
    for idx, k in enumerate(k_filters):
        pos = k.getPosition()
        vel = k.getAbsVelocity()
        width, height = k.getSize()

        if k.validFilter() and not k.selfDestructing():
            homoList.append((pos[0], pos[1], width, height, vel))

        if k.selfDestructing():
            indexList.append(idx)

    # go back to original data to be able to draw boundingbox
    if len(homoList) > 0:
        kalmanResult = doHomography(homoList, invH)

        # Remove invalid kalman filters
        for i in sorted(indexList,reverse=True):
            # Push trajectories to array before deleting filter
            trajectories.append(np.array([k_filters[i].getTrajectoryPath()]))
            del k_filters[i]

        # plot from kalman results
        for left, top, width, height, vel in kalmanResult:
            left, top = int(round(left)), int(round(top))
            v_real = pixVel2realVel(vel,meterPerPixel)
            v_real_str = str(v_real)[:5] + " km/h"
            cv2.rectangle(outFrame, (left, top), (left + width, top + height), (0, 0, 255), 2)
            cv2.putText(currFrame, v_real_str, (left + width + 10, top + height), 0, 1, (0, 0, 255), 2)

    # cv2.imshow('frame', foregroundFrame)
    cv2.imshow('unprocessed_frame', outFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# print(trajectories[0])

# Plot image and all trajectories

# load in image
refImg = cv2.imread("maps3.png", cv2.IMREAD_COLOR)

# genereate random colors in length of trajectories
colorArray = np.random.randint(0, 255, (len(trajectories), 3))

# draw trajectores
for idx, t in enumerate(trajectories):
    # print("########################")
    # print(t)
    cv2.polylines(refImg, t, False, colorArray[idx].tolist(), 4)

# show result
cv2.imshow("trajectories", refImg)

if cv2.waitKey() & 0xFF == ord('q'):
    exit(1)
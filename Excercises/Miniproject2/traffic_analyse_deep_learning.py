from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2

def GetMaskFromAnnotated(annotated):

    #rgbAnnotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

    bgrMin = np.array([0, 0, 255])
    bgrMax = np.array([0, 0, 255])

    maskRGB = cv2.inRange(annotated, bgrMin, bgrMax)
    return maskRGB


cap = cv2.VideoCapture('2017_06_23_1430_Falen_Cigaren_mod_byen.mp4')

prevFrame = None
currFrame = None

annotated = cv2.imread("area_of_operation.png", cv2.IMREAD_COLOR)
annotatedMask = GetMaskFromAnnotated(annotated)

argConfidence = 0.2
argPrototxt = "MobileNetSSD_deploy.prototxt.txt"
argModel = "MobileNetSSD_deploy.caffemodel"

# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(argPrototxt, argModel)

# initialize the video stream, allow the cammera sensor to warmup,
# and initialize the FPS counter
print("[INFO] starting video stream...")
fps = FPS().start()

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)

while cap.isOpened():
    ret, currFrame = cap.read()

    # only keep stuff inside mask from annotation
    #currFrame_mask = cv2.bitwise_and(currFrame, currFrame, mask=annotatedMask)

    frame = imutils.resize(currFrame, width=400)

    # grab the frame dimensions and convert it to a blob
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
                                 0.007843, (300, 300), 127.5)

    # pass the blob through the network and obtain the detections and
    # predictions
    net.setInput(blob)
    detections = net.forward()

    # loop over the detections
    for i in np.arange(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with
        # the prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the `confidence` is
        # greater than the minimum confidence
        if confidence > argConfidence:
            # extract the index of the class label from the
            # `detections`, then compute the (x, y)-coordinates of
            # the bounding box for the object
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # draw the prediction on the frame
            label = "{}: {:.2f}%".format(CLASSES[idx],
                                         confidence * 100)
            cv2.rectangle(frame, (startX, startY), (endX, endY),
                          COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame, label, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

    cv2.imshow('frame', currFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # update the FPS counter
    fps.update()

fps.stop()
cap.release()
cv2.destroyAllWindows()
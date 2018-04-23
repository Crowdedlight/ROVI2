import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import cv2
import numpy as np
from itertools import combinations

from ColorInfo import ColorInfo


def compare_original_and_segmented_image(original, segmented):
    plt.figure(figsize=(9, 3))
    ax1 = plt.subplot(1, 2, 1)
    ax1.imshow(original)
    ax2 = plt.subplot(1, 2, 2, sharex=ax1, sharey=ax1)
    ax2.imshow(segmented)
    plt.show()


def compare_original_and_its_color_channels(original):
    cha1 = original[:, :, 0]
    cha2 = original[:, :, 1]
    cha3 = original[:, :, 2]

    plt.figure(figsize=(9, 2))

    ax1 = plt.subplot(2, 2, 1)
    ax1.imshow(original)
    ax2 = plt.subplot(2, 2, 2, sharex=ax1, sharey=ax1)
    ax2.imshow(cha1, 'gray')
    ax2 = plt.subplot(2, 2, 3, sharex=ax1, sharey=ax1)
    ax2.imshow(cha2, 'gray')
    ax2 = plt.subplot(2, 2, 4, sharex=ax1, sharey=ax1)
    ax2.imshow(cha3, 'gray')

    plt.show()


# Threshold same for every channel
def threshold(img, thres):
    ch1 = img[:, :, 0]
    ch2 = img[:, :, 1]
    ch3 = img[:, :, 2]

    ch1_mask = ch1[:, :] > thres
    ch2_mask = ch2[:, :] > thres
    ch3_mask = ch3[:, :] > thres

    out = img.copy()

    out[:, :, 0] = ch1_mask * img[:, :, 0]
    out[:, :, 1] = ch2_mask * img[:, :, 1]
    out[:, :, 2] = ch3_mask * img[:, :, 2]

    return out


def showImage(img):
    plt.figure(figsize=(6, 4))
    plt.imshow(img)
    plt.show()

#annotated requires to be 255 red
def GetColorInformationFromAnnotated(original, annotated):

    rgbOrg = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    rgbAnnotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

    rgbMin = np.array([255, 0, 0])
    rgbMax = np.array([255, 0, 0])

    maskRGB = cv2.inRange(rgbAnnotated, rgbMin, rgbMax)
    rgbRes = cv2.bitwise_and(rgbOrg, rgbOrg, mask=maskRGB)

    rgbInfo = cv2.meanStdDev(rgbOrg, mask=maskRGB)

    hsvOrg = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
    hsvAnnotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2HSV)

    hsvMin = np.array([0, 255, 255])
    hsvMax = np.array([0, 255, 255])

    maskHSV = cv2.inRange(hsvAnnotated, hsvMin, hsvMax)
    hsvRes = cv2.bitwise_and(hsvOrg, hsvOrg, mask=maskHSV)

    hsvInfo = cv2.meanStdDev(hsvOrg, mask=maskHSV)

    return ColorInfo(rgbInfo[0], rgbInfo[1], hsvInfo[0], hsvInfo[1])
    #print(colorInfo.__dict__)

#segment by distance in rgb colorspace
def SegmentRGBDist(original, refPoint, threshold):

    imgOrg = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)

    #make img of same size with only ref colour
    imgRef = imgOrg.copy()
    imgRef[:, :, 0] = refPoint[0][0]
    imgRef[:, :, 1] = refPoint[1][0]
    imgRef[:, :, 2] = refPoint[2][0]

    #print(imgRef)

    #imgRef = imgRef.astype(np.int16)
    #imgOrg = imgOrg.astype(np.int16)

    #imgDiff = np.subtract(imgOrg, imgRef)

    imgDiff = imgOrg - imgRef #cv2.subtract(imgOrg, imgRef, dtype=cv2.CV_32S)

    # Manhattan distance
    # imgDiff = sum(abs(imgDiff)) #< 200000000
    imgDiff = imgDiff[:,:]

    print(imgDiff)

    compare_original_and_segmented_image(imgOrg, imgDiff)


#### MAIN ####

imgOrg = cv2.imread("Images/DJI_0237.JPG")
imgAnnotated = cv2.imread("Images/DJI_0237_ANNOTATED.png")

# get color information from annotation - Require rgb
colorInfo = GetColorInformationFromAnnotated(imgOrg, imgAnnotated)

#Segment with rgb colorspace distance
SegmentRGBDist(imgOrg, colorInfo.RGBmean, 60)
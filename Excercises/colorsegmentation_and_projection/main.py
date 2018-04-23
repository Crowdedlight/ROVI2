import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import cv2
import numpy as np


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


img = cv2.imread('../../Images/DJI_0006.JPG')
#showImage(img)

# cvt to RGB instead of BGR
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Excercise 1 - find pixels satuated in all color channels and every single channel
r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]
r_saturated = r[:, :] > 254
g_saturated = g[:, :] > 254
b_saturated = b[:, :] > 254

# count numbers of overexposed elements
r_values = cv2.sumElems(1.0*r_saturated)
g_values = cv2.sumElems(1.0*g_saturated)
b_values = cv2.sumElems(1.0*b_saturated)
#total_values = cv2.sumElems(1.0*)

print("r oversatuated: %d" % r_values[0])
print("g oversatuated: %d" % g_values[0])
print("b oversatuated: %d" % b_values[0])

#compare_original_and_its_color_channels(img)
thresImg = threshold(img, 190)
#compare_original_and_segmented_image(img, thresImg)

#convert to hsv
imgHSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

#compare_original_and_its_color_channels(imgHSV)

#segment on value channel
h = imgHSV[:, :, 0]
s = imgHSV[:, :, 1]
v = imgHSV[:, :, 2]

BALLS_MIN = np.array([0, 0, 150],np.uint8)
BALLS_MAX = np.array([180, 255, 255],np.uint8)

(T, thresImg) = cv2.threshold(imgHSV, 150, 255, cv2.THRESH_BINARY)
thresImg = cv2.inRange(imgHSV, BALLS_MIN, BALLS_MAX);

compare_original_and_segmented_image(img, thresImg)

point = [40, 255, 240]
print(np.linalg.norm(point))
thres = 80

#test = (np.linalg.norm(imgHSV[:, :], None, 2) - np.linalg.norm(point)) < thres
#test = np.linalg.norm(imgHSV[:, :], None, 2)
#print(test)

#test = 1.0*test*imgHSV
#compare_original_and_segmented_image(img, test)

# while cv2.waitKey() != 27:
#     pass


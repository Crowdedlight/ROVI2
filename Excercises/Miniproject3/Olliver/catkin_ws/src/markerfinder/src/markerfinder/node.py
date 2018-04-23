#!/usr/bin/env python
import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from std_msgs.msg import Int16
from std_msgs.msg import Float32
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from MarkerTracker import MarkerTracker
import numpy as np
from markerfinder.msg import MarkerLocation


class image_converter:
    def __init__(self):
        # Publish to the MarkerLocator's original topic
        self.image_pub = rospy.Publisher("/markerlocator/image_raw", Image)
        self.marker_pose_pub = rospy.Publisher("/markerlocator/markerpose", MarkerLocation)

        # Subscribe from the Iris camera topic
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/iris/camera/image_raw", Image, self.callback)

    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        # Display the image
        # cv2.imshow("Image window", cv_image)

        frame_gray = cv2.cvtColor(cv_image, cv2.COLOR_RGB2GRAY)
        order = 10
        kernel_size = 25
        scale_factor = 100
        mt = MarkerTracker(order, kernel_size, scale_factor)
        self.pose = mt.locate_marker(frame_gray)
        cv2.rectangle(frame_gray, (self.pose.x + 100, self.pose.y + 100), (self.pose.x - 100, self.pose.y - 100),
                      (0, 255, 0), 3)

        # cv2.imshow("Box",cv_image)
        # cv2.waitKey(3)
        # print("{} {} {} {} {} {}".format("x-pose:", self.pose.x, "y-pose:", self.pose.y, "theta:", self.pose.theta))
        height, width = cv_image.shape[:2]
        try:
            # position out
            currX = self.pose.x - (width / 2)
            currY = self.pose.y - (height / 2)
            msg = MarkerLocation(x = currX, y = currY, theta = self.pose.theta)
            self.marker_pose_pub.publish(msg)

            #camera feed with marker detection
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(frame_gray, '8UC1'))
        except CvBridgeError as e:
            print(e)


def main():
    rospy.init_node('markerfinder', anonymous=True)
    ic = image_converter()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

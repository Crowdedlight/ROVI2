#!/usr/bin/env python
import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from std_msgs.msg import Int16
from std_msgs.msg import Float32
import numpy as np


def main():
	rospy.init_node('droneinfo', anonymous=True)
	while not rospy.is_shutdown():
        print "test"


if __name__ == '__main__':
	main()
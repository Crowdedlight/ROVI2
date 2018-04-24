#!/usr/bin/env python
import roslib
import sys
import rospy
from geometry_msgs.msg import PoseStamped
from image_tools import getGSD
from std_msgs.msg import Float32


class droneinfo:
	def __init__(self):
		# Publish to the MarkerLocator's original topic
		self.gsd = rospy.Publisher("/droneinfo/gsd", Float32, queue_size=10)
		self.currGSD = 0

		# Parameters depending on camera
		self.fov = 1.3962634
		self.pixel_width = 800

		# Subscribe to get height
		self.image_sub = rospy.Subscriber("/mavros/local_position/pose", PoseStamped, self.callback)

	def callback(self, data):
		height = data.pose.position.z
		self.currGSD = getGSD(height, self.fov, self.pixel_width)
		self.gsd.publish(self.currGSD)


def main():
	rospy.init_node('droneinfo', anonymous=True)
	di = droneinfo()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")

if __name__ == '__main__':
	main()

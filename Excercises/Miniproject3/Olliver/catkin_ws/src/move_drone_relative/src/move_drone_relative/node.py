import rospy
from move_drone_relative.msg import MoveDrone
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import SetMode, CommandBool
from std_srvs.srv import Trigger
from genpy.message import fill_message_args
from math import cos, sin, pi, atan2, asin, degrees
from quaternion import *
import numpy as np
from numpy.linalg import inv

class DroneMove:

	def __init__(self):
		self.current_state = State()
		self.current_pose = PoseStamped()
		self.next_pose = PoseStamped()

		rospy.Subscriber("mavros/state", State, self.cb_state)
		rospy.Subscriber("mavros/local_position/pose", PoseStamped, self.cb_print_orientation)
		rospy.Subscriber("move_drone_relative/set_relative_pose", MoveDrone, self.move_handler)

		self.pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size=10)

		self.arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)
		self.set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)
		self.rate = rospy.Rate(10)


	def connect(self):
		yaw = 0 * pi / 180
		roll = 0 * pi / 180
		pitch = 0 * pi / 180

		q = euler_angle_2_quaternion(roll, pitch, yaw)
		print("Quaternion: {}".format(q))
		self.next_pose = PoseStamped()
		args = [{'pose': {'position': [0, 0, 2], 'orientation': [q.x, q.y, q.z, q.w]}}]
		fill_message_args(self.next_pose, args)

		while not rospy.is_shutdown() and not self.current_state.connected:
			self.rate.sleep()

		# you must publish set points to the drone before you can change the mode
		for i in range(1, 10):
			self.pub.publish(self.next_pose)
			self.rate.sleep()

		self.set_mode_client(custom_mode="OFFBOARD")
		self.arming_client(value=True)

	def run(self):
		while not rospy.is_shutdown():
			self.pub.publish(self.next_pose)
			self.rate.sleep()

	def cb_print_orientation(self, data):
		self.current_pose = data

	def cb_state(self, data):
		self.current_state = data
		# rospy.loginfo(data)


	def move_handler(self, req):
		X =req.x
		Y =req.y
		Z =req.z
		yaw = req.yaw * pi / 180

		print(self.current_pose)

		world2drone = posestamped_to_transform(self.current_pose)
		transform = transformation_matrix(self.current_pose.pose.orientation, X, Y, Z, yaw)

		# matrix_to_posestamped(transform)
		# print(transform)

		translation = np.array([[X],[Y],[Z],[1]])

		new_pos = np.matmul(world2drone,translation)
		# new_conf = np.matmul(world2drone,transform)
		# global pose
		# pose = matrix_to_posestamped(new_conf)
		# # print(new_conf)

		rospy.loginfo("Yawing {} degrees".format(yaw*180/pi))

		q = perform_yaw(self.current_pose, yaw)
		args = [{'pose': {'position': [new_pos[0],new_pos[1],new_pos[2]],
						  'orientation': [q.x, q.y, q.z, q.w]} }]
		fill_message_args(self.next_pose, args)
		# w, x, y, z = euler_angle_2_quaternion(roll, pitch, yaw)
		# delta_pose = PoseStamped()
		# args = [{'pose': {'position': [0, 0, 2], 'orientation': [x, y, z, w]}}]
		# fill_message_args(delta_pose, args)
		#
		# global pose
		# pose = PoseStamped()
		#
		# w, x, y, z = quaternion_mult(current_pose.pose.orientation, delta_pose.pose.orientation)
		# args = [{'pose': {'position': [new_pos[0], new_pos[1], new_pos[2]], 'orientation': [x, y, z, w]}}]
		# fill_message_args(pose, args)


def main():
	rospy.init_node("python_node")

	drone = DroneMove()
	drone.connect()
	drone.run()

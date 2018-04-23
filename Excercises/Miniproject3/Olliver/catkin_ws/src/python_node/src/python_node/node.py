import rospy
from python_node.msg import MoveDrone
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import SetMode, CommandBool
from genpy.message import fill_message_args
from math import cos, sin, pi, atan2, asin, degrees
from quaternion import *
import numpy as np
from numpy.linalg import inv

current_state = State()
current_pose = PoseStamped()
pose = PoseStamped()

def cb_print_orientation(data):
	global current_pose
	current_pose = data

def callback(data):
	global current_state
	current_state = data
	rospy.loginfo(data)


def main():
	rospy.init_node("python_node")
	rospy.Subscriber("mavros/state", State, callback)
	rospy.Subscriber("mavros/local_position/pose", PoseStamped, cb_print_orientation)

	pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size=10)

	rate = rospy.Rate(10)

	while not rospy.is_shutdown() and not current_state.connected:
		rate.sleep()

	arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)
	set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)

	yaw = 0 * pi / 180
	roll = 0 * pi / 180
	pitch = 0 * pi / 180

	q = euler_angle_2_quaternion(roll,pitch,yaw)
	print("Quaternion: {}".format(q))
	global pose
	pose = PoseStamped()
	args = [{'pose': {'position': [0,0,2], 'orientation': [q.x, q.y, q.z, q.w]} }]
	fill_message_args(pose, args)

	rospy.loginfo(pose)

	# you must publish set points to the drone before you can change the mode
	for i in range(1,10):
		pub.publish(pose)
		rate.sleep()

	set_mode_client(custom_mode="OFFBOARD")
	arming_client(value=True)

	def service_handler(req):
		X =req.x
		Y =req.y
		Z =req.z
		yaw = req.yaw * pi / 180

		print(current_pose)

		world2drone = posestamped_to_transform(current_pose)
		transform = transformation_matrix(current_pose.pose.orientation,X,Y,Z,yaw)

		# matrix_to_posestamped(transform)
		# print(transform)

		translation = np.array([[X],[Y],[Z],[1]])

		new_pos = np.matmul(world2drone,translation)
		# new_conf = np.matmul(world2drone,transform)
		# global pose
		# pose = matrix_to_posestamped(new_conf)
		# # print(new_conf)

		rospy.loginfo("Yawing {} degrees".format(yaw*180/pi))

		global pose
		q = perform_yaw(current_pose, yaw)
		args = [{'pose': {'position': [new_pos[0],new_pos[1],new_pos[2]],
						  'orientation': [q.x, q.y, q.z, q.w]} }]
		fill_message_args(pose,args)
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


		return True

	rospy.Subscriber("move_drone", MoveDrone, service_handler)
	# rospy.Service("move_drone",MoveDrone,service_handler)

	while not rospy.is_shutdown():
		pub.publish(pose)
		rate.sleep()

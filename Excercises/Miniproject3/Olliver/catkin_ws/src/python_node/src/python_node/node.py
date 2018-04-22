import rospy
from python_node.srv import Yaw
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import SetMode, CommandBool
from genpy.message import fill_message_args
from math import cos, sin, pi, atan2, asin, degrees
from quaternion import *

current_state = State()
current_pose = PoseStamped()
pose = PoseStamped()

def cb_print_orientation(data):
	# q0 = data.pose.orientation.w
	# q1 = data.pose.orientation.x
	# q2 = data.pose.orientation.y
	# q3 = data.pose.orientation.z
	# roll, pitch, yaw = quaternion_to_euler_angle(q0,q1,q2,q3)
	global current_pose
	current_pose = data

def callback(data):
	global current_state
	current_state = data
	#rospy.loginfo(data)


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

	w, x, y, z = euler_angle_2_quaternion(roll,pitch,yaw)
	global pose
	pose = PoseStamped()
	args = [{'pose': {'position': [0,0,2], 'orientation': [x,y,z,w]} }]
	fill_message_args(pose, args)

	rospy.loginfo(pose)

	# you must publish set points to the drone before you can change the mode
	for i in range(1,10):
		pub.publish(pose)
		rate.sleep()

	set_mode_client(custom_mode="OFFBOARD")
	arming_client(value=True)

	def handler(req):
		yaw = req.yaw * pi / 180
		rospy.loginfo("Yawing {} degrees".format(yaw*180/pi))
		w, x, y, z = euler_angle_2_quaternion(roll, pitch, yaw)
		delta_pose = PoseStamped()
		args = [{'pose': {'position': [0, 0, 2], 'orientation': [x, y, z, w]}}]
		fill_message_args(delta_pose, args)

		global pose
		pose = PoseStamped()

		w, x, y, z = quaternion_mult(current_pose.pose.orientation, delta_pose.pose.orientation)
		args = [{'pose': {'position': [0, 0, 2], 'orientation': [x, y, z, w]}}]
		fill_message_args(pose, args)

		return True

	rospy.Service("turn_drone",Yaw,handler)

	while not rospy.is_shutdown():
		pub.publish(pose)
		rate.sleep()

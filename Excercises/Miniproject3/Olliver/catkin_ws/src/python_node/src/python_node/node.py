import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import SetMode, CommandBool
from math import cos, sin, pi, atan2, asin, degrees

current_state = State()


def quaternion_to_euler_angle(w, x, y, z):
	ysqr = y * y

	t0 = +2.0 * (w * x + y * z)
	t1 = +1.0 - 2.0 * (x * x + ysqr)
	X = degrees(atan2(t0, t1))

	t2 = +2.0 * (w * y - z * x)
	t2 = +1.0 if t2 > +1.0 else t2
	t2 = -1.0 if t2 < -1.0 else t2
	Y = degrees(asin(t2))

	t3 = +2.0 * (w * z + x * y)
	t4 = +1.0 - 2.0 * (ysqr + z * z)
	Z = degrees(atan2(t3, t4))

	return X, Y, Z

def quaternion2yaw(pose):
	q0 = pose.pose.orientation.w
	q1 = pose.pose.orientation.x
	q2 = pose.pose.orientation.y
	q3 = pose.pose.orientation.z


	return atan2(2*(q0*q3+q1*q2), 1 - 2*(q2**2+q3**2))

def cb_print_orientation(data):
	q0 = data.pose.orientation.w
	q1 = data.pose.orientation.x
	q2 = data.pose.orientation.y
	q3 = data.pose.orientation.z
	roll, pitch, yaw = quaternion_to_euler_angle(q0,q1,q2,q3)

	rospy.loginfo("R: {} P: {} Y: {}".format(roll,pitch,yaw))

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

	pose = PoseStamped()
	pose.pose.position.x = 0
	pose.pose.position.y = 0
	pose.pose.position.z = 2

	yaw = 210 * pi / 180
	roll = 0 * pi / 180
	pitch = 0 * pi / 180

	cy = cos(yaw * 0.5)
	sy = sin(yaw * 0.5)
	cr = cos(roll * 0.5)
	sr = sin(roll * 0.5)
	cp = cos(pitch * 0.5)
	sp = sin(pitch * 0.5)

	pose.pose.orientation.w = cy * cr * cp + sy * sr * sp
	pose.pose.orientation.x = cy * sr * cp - sy * cr * sp
	pose.pose.orientation.y = cy * cr * sp + sy * sr * cp
	pose.pose.orientation.z = sy * cr * cp - cy * sr * sp

	# you must publish set points to the drone before you can change the mode
	for i in range(1,10):
		pub.publish(pose)
		rate.sleep()

	set_mode_client(custom_mode="OFFBOARD")
	arming_client(value=True)

	while not rospy.is_shutdown():

		pub.publish(pose)
		rate.sleep()



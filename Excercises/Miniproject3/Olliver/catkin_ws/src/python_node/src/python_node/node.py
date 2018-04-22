import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import SetMode, CommandBool
from math import cos, sin, pi, atan2, asin, degrees

current_state = State()
current_pose = PoseStamped()

def euler_angle_2_quaternion(R,P,Y):
	cr = cos(R * 0.5)
	sr = sin(R * 0.5)
	cp = cos(P * 0.5)
	sp = sin(P * 0.5)
	cy = cos(Y * 0.5)
	sy = sin(Y * 0.5)

	w = cy * cr * cp + sy * sr * sp
	x = cy * sr * cp - sy * cr * sp
	y = cy * cr * sp + sy * sr * cp
	z = sy * cr * cp - cy * sr * sp

	return w, x, y, z

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

def quaternion_mult(q1,q2):
	w = q1.w*q2.w - q1.x*q2.x - q1.y*q2.y - q1.z*q2.z
	x = q1.w*q2.x + q1.x*q2.w + q1.y*q2.z - q1.z*q2.y
	y = q1.w*q2.y + q1.y*q2.w + q1.z*q2.x - q1.x*q2.z
	z = q1.w*q2.z + q1.z*q2.w + q1.x*q2.y - q1.y*q2.x

	return w, x, y, z

def cb_print_orientation(data):
	q0 = data.pose.orientation.w
	q1 = data.pose.orientation.x
	q2 = data.pose.orientation.y
	q3 = data.pose.orientation.z
	roll, pitch, yaw = quaternion_to_euler_angle(q0,q1,q2,q3)

	global current_pose
	current_pose = data

	rospy.loginfo("Yaw Angle: {}".format(yaw))

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
	delta_pose = PoseStamped(

	)
	pose.pose.position.x = 0
	pose.pose.position.y = 0
	pose.pose.position.z = 2

	yaw = 210 * pi / 180
	roll = 0 * pi / 180
	pitch = 0 * pi / 180

	w, x, y, z = euler_angle_2_quaternion(roll,pitch,yaw)

	pose.pose.orientation.w = w
	pose.pose.orientation.x = x
	pose.pose.orientation.y = y
	pose.pose.orientation.z = z

	yaw = 10 * pi / 180
	w, x, y, z = euler_angle_2_quaternion(roll,pitch,yaw)
	delta_pose.pose.position.x = 0
	delta_pose.pose.position.y = 0
	delta_pose.pose.position.z = 0
	delta_pose.pose.orientation.w = w
	delta_pose.pose.orientation.x = x
	delta_pose.pose.orientation.y = y
	delta_pose.pose.orientation.z = z
	# you must publish set points to the drone before you can change the mode
	for i in range(1,10):
		pub.publish(pose)
		rate.sleep()

	set_mode_client(custom_mode="OFFBOARD")
	arming_client(value=True)

	while not rospy.is_shutdown():

		w, x, y, z = quaternion_mult(current_pose.pose.orientation, delta_pose.pose.orientation)
		pose.pose.orientation.w = w
		pose.pose.orientation.x = x
		pose.pose.orientation.y = y
		pose.pose.orientation.z = z
		pub.publish(pose)
		rate.sleep()



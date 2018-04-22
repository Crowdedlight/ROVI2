import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import SetMode, CommandBool

global current_state

def callback(data):
	current_state = data
	rospy.loginfo(data)

def main():
	rospy.init_node("python_node")
	rospy.Subscriber("mavros/state", State, callback)

	pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped,queue_size=10)

	set_mode_client = rospy.ServiceProxy("mavros/set_mode",SetMode)
	set_mode_client(custom_mode="OFFBOARD")

	arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)
	arming_client(value=True)

	rate = rospy.Rate(10)

	pose = PoseStamped()
	pose.pose.position.x = -3
	pose.pose.position.y = 5
	pose.pose.position.z = 3

	while not rospy.is_shutdown():
		pub.publish(pose)
		rate.sleep()

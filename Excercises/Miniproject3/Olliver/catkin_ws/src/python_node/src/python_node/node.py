import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
import genpy
import rosservice
import roslib.packages

def callback(data):
	rospy.loginfo(data)

def main():
	rospy.init_node("python_node")
	rospy.Subscriber("mavros/state", State, callback)
	rospy.spin()

#!/usr/bin/env python

"""Example of a ROS node using Python's OO features.  The node is
represented as a class.  Sensor messages are stored in instance
variables.

Author: Nathan Sprague
Version: 9/8/2015

"""
import rospy

from geometry_msgs.msg import Point
from geometry_msgs.msg import Vector3

class ThrusterNode(object):
    def __init__(self):
        rospy.init_node('thruster')

        self.location = None # Stores recently received location messages.
        rospy.Subscriber('location', Point, self.location_callback)

        self.thrust_pub = rospy.Publisher('thrust', Vector3, queue_size=1)

        self.location = None
        self.target_altitude = 100.0

    def location_callback(self, loc_msg):
        """ loc_msg will be of type Point """
        self.location = loc_msg

    def run(self):
        """ The main loop for this node. """
        thrust = Vector3()
        rate = rospy.Rate(10)

        # Spin until the first location message is available.
        while self.location is None and not rospy.is_shutdown():
            rospy.sleep(.1)

        while not rospy.is_shutdown():
            if self.location.y < self.target_altitude:
                thrust.y = 100.0
                rospy.loginfo("THRUSTERS ENGAGED")
            else:
                thrust.y = 0.0

            self.thrust_pub.publish(thrust)
            rate.sleep()

if __name__ == "__main__":
    node = ThrusterNode()
    node.run()

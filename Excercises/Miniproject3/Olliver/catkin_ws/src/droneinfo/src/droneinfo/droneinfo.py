#!/usr/bin/env python
import roslib
import sys
import rospy
from geometry_msgs.msg import PoseStamped
from rospy.impl import init

from image_tools import getGSD
from std_msgs.msg import Float32
from std_srvs.srv import SetBool, SetBoolRequest, SetBoolResponse
import time
import csv
from quaternion import *


class droneinfo:
    def __init__(self):
        # Publish to the MarkerLocator's original topic
        self.gsd = rospy.Publisher("/droneinfo/gsd", Float32, queue_size=10)
        self.currGSD = 0

        # Parameters depending on camera
        self.fov = 1.3962634
        self.pixel_width = 800

        # Service handler
        self.s_start_log = rospy.Service("/droneinfo/start_logging", SetBool, self.startLogHandler, buff_size=10)
        self.s_stop_log = rospy.Service("/droneinfo/stop_logging", SetBool, self.stopLogHandler, buff_size=10)
        self.s_save_log = rospy.Service("/droneinfo/save_log", SetBool, self.saveLogHandler, buff_size=10)

        # loggin parameters
        self.timeStart = rospy.get_time()
        self.logging = False
        self.logfile = "src/droneinfo/logs/log" + "_" + time.strftime("%d_%m_%Y") + "_" + time.strftime("%H_%M_%S") + ".csv"
        # log in memory
        self.loglist = []

        # Subscribe to get height
        self.image_sub = rospy.Subscriber("/mavros/local_position/pose", PoseStamped, self.callback)

    def startLogHandler(self, msg):
            self.logging = True
            self.timeStart = rospy.get_time()
            self.loglist = []
            return SetBoolResponse(success=True, message="Logging Started")

    def stopLogHandler(self, msg):
        self.logging = False
        return SetBoolResponse(success=True, message="Logging Stopped")

    def saveLogHandler(self, msg):
        print("saving logfile")

        if len(self.loglist) == 0:
            return SetBoolResponse(success=False, message="Log is empty, nothing to save")

        with open(self.logfile, 'w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            for val in self.loglist:
                spamwriter.writerow(val)

        self.logging = False
        self.loglist = []

        return SetBoolResponse(success=True, message="Log Saved to file")

    def callback(self, data):
        height = data.pose.position.z
        self.currGSD = getGSD(height, self.fov, self.pixel_width)
        self.gsd.publish(self.currGSD)

        # save to log file in memory
        if self.logging:
            q = data.pose.orientation
            _, _, yaw = quaternion_to_euler_angle(q.w, q.x, q.y, q.z)
            deltaT = rospy.get_time() - self.timeStart
            
            data = [deltaT, data.pose.position.x, data.pose.position.y, data.pose.position.z, yaw]
            self.loglist.append(data)

    def shutdownHandler(self):
        self.saveLogHandler(None)

        # shutdown services
        self.s_save_log.shutdown()
        self.s_start_log.shutdown()
        self.s_stop_log.shutdown()
        print("Shutting down")


def main():
    rospy.init_node('droneinfo', anonymous=True)
    rospy.sleep(1)

    di = droneinfo()

    rospy.on_shutdown(di.shutdownHandler)

    rospy.spin()

if __name__ == '__main__':
    main()

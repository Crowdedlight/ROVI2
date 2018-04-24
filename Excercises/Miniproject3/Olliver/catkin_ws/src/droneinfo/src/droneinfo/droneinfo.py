#!/usr/bin/env python
import roslib
import sys
import rospy
from geometry_msgs.msg import PoseStamped
from rospy.impl import init

from image_tools import getGSD
from std_msgs.msg import Float32, Bool
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
        self.s_start_log = rospy.Service("start_logging", Bool, self.startLogHandler, buff_size=10)
        self.s_stop_log = rospy.Service("stop_logging", Bool, self.stopLogHandler, buff_size=10)
        self.s_save_log = rospy.Service("save_logging", Bool, self.saveLogHandler, buff_size=10)

        # loggin parameters
        self.timeStart = rospy.get_time()
        self.logging = False
        self.logfile = "src/droneinfo/logs/log" + "_" + time.strftime("%d_%m_%Y") + "_" + time.strftime("%H_%M_%S") + ".csv"
        # log in memory
        self.loglist = []

        # Subscribe to get height
        self.image_sub = rospy.Subscriber("/mavros/local_position/pose", PoseStamped, self.callback)


    def startLogHandler(self):
        self.logging = True
        self.timeStart = rospy.get_time()
        self.loglist = []
        return "Logging Started"

    def stopLogHandler(self):
        self.logging = False
        return "Logging Stopped"

    def saveLogHandler(self):
        print("saving logfile")

        if len(self.loglist) == 0:
            print("Log is empty, nothing to save")
            return

        with open(self.logfile, 'w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            for val in self.loglist:
                spamwriter.writerow(val)

        self.logging = False
        self.loglist = []

        print("file saved")

        return "Log saved to file"

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
        self.saveLogHandler()
        print("Shutting down")


def main():
    rospy.init_node('droneinfo', anonymous=True)
    rospy.sleep(1)

    di = droneinfo()

    rospy.on_shutdown(di.shutdownHandler)

    rospy.spin()

if __name__ == '__main__':
    main()

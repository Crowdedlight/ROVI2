#!/usr/bin/env python
import roslib
import sys
import rospy
import rospkg
from geometry_msgs.msg import PoseStamped
from rospy.impl import init

from image_tools import getGSD
from std_msgs.msg import Float32
from std_srvs.srv import Trigger, TriggerResponse
from droneinfo.srv import StartLogging, StartLoggingResponse

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
        self.s_start_log = rospy.Service("/droneinfo/start_logging", StartLogging, self.startLogHandler, buff_size=10)
        self.s_stop_log = rospy.Service("/droneinfo/stop_logging", Trigger, self.stopLogHandler, buff_size=10)

        # loggin parameters
        self.timeStart = rospy.get_time()
        self.logging = False
        self.userSetLogName = ""
        rospack = rospkg.RosPack()
        self.path = rospack.get_path('droneinfo')
        self.logfile = self.path + "/logs/log" + "_" + self.userSetLogName + time.strftime(
            "%d_%m_%Y") + "_" + time.strftime("%H_%M_%S") + ".csv"
        # log in memory
        self.loglist = []

        # Subscribe to get height
        self.image_sub = rospy.Subscriber("/mavros/local_position/pose", PoseStamped, self.callback)

    # need to use function to get latest changes set from services. Also updates self.logname
    def updateLogName(self):
        self.logfile = self.path + "/logs/log" + "_" + self.userSetLogName + time.strftime(
            "%d_%m_%Y") + "_" + time.strftime("%H_%M_%S") + ".csv"

    def startLogHandler(self, req):
        # if req != empty, change logfile name
        if req.logname != "":
            self.userSetLogName = req.logname + "_"

        # update logname for correct time and custom tag
        self.updateLogName()
        self.logging = True
        self.loglist = []
        return StartLoggingResponse(success=True, message="Logging Started")

    def stopLogHandler(self, req):

        # always stop logging
        self.logging = False

        if len(self.loglist) == 0:
            print("Log is empty, nothing to save")
            return TriggerResponse(success=False, message="Log is empty, nothing to save")

        with open(self.logfile, 'w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            for val in self.loglist:
                spamwriter.writerow(val)

        # clear log in memory
        self.loglist = []
        return TriggerResponse(success=True, message="Logging Stopped and saved to file: " + self.logfile)

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
        self.stopLogHandler(None)

        # shutdown services
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

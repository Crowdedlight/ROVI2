#!/usr/bin/env python
from time import time, strftime
import os

# sys.path.append('/opt/ros/indigo/lib/python2.7/dist-packages')
# need to run the following line before running the script in ros mode
# source /opt/ros/indigo/setup.bash

# python imports
import signal
import cv2
import math
import numpy as np

# application imports
from PerspectiveTransform import PerspectiveCorrecter
from MarkerTracking/MarkerPose import MarkerPose
from MarkerTracking/MarkerPosemarker_tester import MarkerTracker

# parameters
print_debug_messages = False
show_image = True
list_of_markers_to_find = [5, 6]
get_images_to_flush_cam_buffer = 5
publish_to_ros = False
markerpose_ros_topic = '/markerlocator/markerpose'

# global variables
stop_flag = False
### Locate a single marker in an image

# python imports
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as pltColor
import signal
import cv2
import math
import numpy as np

# application imports
from MarkerTracker import MarkerTracker
import img

# parameters
print_debug_messages = False
show_image = True
list_of_markers_to_find = [3]
get_images_to_flush_cam_buffer = 5
publish_to_ros = False
markerpose_ros_topic = '/markerlocator/markerpose'

# global variables
stop_flag = False

# define ctrl-c handler
'''
def signal_handler(signal, frame):
	global stop_flag
	stop_flag = True 
'''


# install ctrl-c handler
#signal.signal(signal.SIGINT, signal_handler)


# main function
if __name__ == "__main__":
	print "Running.."

	print 'Loading image..'
	img = cv2.imread('marker_image.jpg', 0)
	''' plt.imshow(img, cmap='gray', interpolation='bicubic')
	#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
	#plt.show()
	#print "image plotted.." '''

	# Number of n-fold edges:
	order = 3
	kernel_size = 25
	scale_factor = 100

	#print 'Finding marker..'
	mt = MarkerTracker(order, kernel_size, scale_factor)
	while True:
		mt.locate_marker(img)
		mt.determine_marker_orientation(img)
		mt.determine_marker_quality(img)
		#print 'Marker found..'

		#print 'Plotting marker..'
		#img2 = mt.extract_window_around_maker_location(img)
		#plt.imshow(img2, cmap='gray', interpolation='bicubic')
		#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
		#plt.show()


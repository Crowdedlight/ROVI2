
from time import time, strftime
import os
import signal
import cv2
from cv2 import aruco
import math
import numpy as np
import yaml

class VideoMarkerFinder:

	def __init__(self, dict, video_device):
		self.camera = cv2.VideoCapture(video_device)
		#self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
		#self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
		self.aruco_dict = dict
		self.arucoParams = aruco.DetectorParameters_create()
		self.running = True

		ret, self.current_frame = self.camera.read()
		self.t0 = time()
		self.t1 = time()

		self.markers_detected = False

		self.calibrated = True
		if self.calibrated:
			self.maker_length = 7
			self.calibration()

	def do_the_magic(self):
		self.find_markers()
		self.draw_markers()
		self.show_video_with_markers()

	def calibration(self):
		with open('calibration.yaml') as f:
			self.calibration_params = yaml.load(f)
		self.camera_matrix = np.array(self.calibration_params.get('camera_matrix'))
		self.dist_coeffs = np.array(self.calibration_params.get('dist_coeff'))
		self.image_height = self.calibration_params.get('height')
		self.image_width = self.calibration_params.get('width')
		image_size = (self.image_width, self.image_height)
		self.newcameramtx, self.roi = cv2.getOptimalNewCameraMatrix(self.camera_matrix, self.dist_coeffs, image_size, 1, image_size)
		self.map1, self.map2 = cv2.initUndistortRectifyMap(self.camera_matrix, self.dist_coeffs, None, self.newcameramtx, image_size, 5)

	def find_markers(self):
		ret, self.current_frame = self.camera.read()
		if self.calibrated:
			img_remapped = cv2.remap(self.current_frame, self.map1, self.map2, cv2.INTER_LINEAR)
			self.corners, self.ids, self.rejected_img_points = aruco.detectMarkers(img_remapped, self.aruco_dict,
																				   parameters=self.arucoParams)
		else:
			self.corners, self.ids, self.rejected_img_points = aruco.detectMarkers(self.current_frame, self.aruco_dict,
																				   parameters=self.arucoParams)
		if self.corners:
			self.markers_detected = True
		else:
			self.markers_detected = False

	def draw_markers(self):
		self.img_with_aruco = aruco.drawDetectedMarkers(self.current_frame, self.corners, self.ids, (255, 0, 255))

		if self.calibrated and self.markers_detected:
			(self.t1, self.t0) = (self.t0, time())
			self.time_diff = self.t0 - self.t1
			for i in range(len(self.ids)):
				self.rvec, self.tvec, _objPoints = aruco.estimatePoseSingleMarkers(self.corners[i], self.maker_length,
																		 self.camera_matrix, self.dist_coeffs)
				self.img_with_aruco = aruco.drawAxis(self.img_with_aruco, self.camera_matrix,
													 self.dist_coeffs, self.rvec, self.tvec, 6)
				self.calc_rotation_and_translation_matrix()
				self.some_vec = np.cross(self.rmat[:,0], self.rmat[:,2])
				print self.rvec
				#print 'marker{}'.format(i)
				#print tvec

	def calc_rotation_and_translation_matrix(self):
		self.rmat, _ = cv2.Rodrigues(self.rvec)
		self.tmat, _ = cv2.Rodrigues(self.tvec)

	def show_video_with_markers(self):
		cv2.imshow('Markers', self.img_with_aruco)

	def handle_keyboard_events(self):
		# Listen for keyboard events and take relevant actions.
		key = cv2.waitKey(1)
		# Discard higher order bit, http://permalink.gmane.org/gmane.comp.lib.opencv.devel/410
		key = key & 0xff
		if key == 27:  # Esc
			self.running = False
		if key == 114:  # R
			print("Resetting...")
		if key == 115:  # S
			# save image
			print("Saving image...")
			filename = strftime("%Y-%m-%d %H-%M-%S")
			cv2.imwrite("output/%s.png" % filename, self.current_frame)

	def close_all_windows(self):
		self.camera.release()
		cv2.destroyAllWindows()


if __name__ == "__main__":
	print 'Starting...'

	videoDevice = 1
	aruco_dict = aruco.Dictionary_get(aruco.DICT_7X7_250)
	vmf = VideoMarkerFinder(aruco_dict, videoDevice)

	while vmf.running == True:
		vmf.do_the_magic()
		vmf.handle_keyboard_events()

	# When everything done, release the capture
	vmf.close_all_windows()
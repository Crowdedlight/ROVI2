from time import time, strftime
import cv2


running = False
current_frame = None

if __name__ == "__main__":
	print 'Starting...'

	running = True
	camera = cv2.VideoCapture(1)
	camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
	camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

	while running == True:
		ret, current_frame = camera.read()
		cv2.imshow('img', current_frame)
		key = cv2.waitKey(1)
		# Discard higher order bit, http://permalink.gmane.org/gmane.comp.lib.opencv.devel/410
		key = key & 0xff
		if key == 27:  # Esc
			running = False
		if key == 115:  # S
			# save image
			print("Saving image...")
			filename = strftime("%Y-%m-%d %H-%M-%S")
			cv2.imwrite("output/%s.png" % filename, current_frame)

	camera.release()
	cv2.destroyAllWindows()
import rospy
from move_drone_relative.msg import MoveDrone
from markerfinder.msg import MarkerLocation
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Float32
from time import time
from math import pi
import numpy as np

class Controller:
	def __init__(self):
		self.setpoint_pub = rospy.Publisher("/move_drone_relative/set_relative_pose", MoveDrone,queue_size=10)

		rospy.Subscriber("mavros/local_position/pose", PoseStamped, self.cb_control_loop)
		rospy.Subscriber("markerlocator/markerpose", MarkerLocation, self.cb_update_setpoint)
		rospy.Subscriber("droneinfo/gsd", Float32, self.cb_update_GSD)

		self.GSD = 2.0/800
		self.setpoint = None
		self.command = MoveDrone()
		self.height_setpoint = 5
		self.current_height = 2

		self.P = 0.8
		self.I = 0#.0002
		self.D = 0#.0009

		self.int_sum = np.array([[0],[0],[0],[0]])
		self.prev_error = np.array([[0],[0],[0],[0]])
		self.prev_time = None

	def cb_control_loop(self, msg):
		self.current_height = msg.pose.position.z
		#print(msg)

	def cb_update_setpoint(self, msg):
		x = msg.x
		y = msg.y
		theta = msg.theta * 180 / pi
		quality = msg.quality

		# the camera is not aligned with the drone
		x_error = -y*self.GSD
		y_error = -x*self.GSD
		z_error = self.height_setpoint - self.current_height
		angle_error = 0

		# if abs(x_error) < 1 and abs(y_error) < 1 and abs(z_error) < 1:
		angle_error = (-theta - 90)*self.P

		if abs(angle_error) < 0.1 and abs(x_error) < 0.1 and abs(y_error) < 0.1:
			self.height_setpoint = 0


		cmd = self.pid_control(x_error,y_error,z_error,angle_error)

		print("{}, {}, {}, {}".format(x_error,y_error,z_error,angle_error))

		command = MoveDrone(x = cmd[0],#x_error,
							y = cmd[1],#y_error,
							z = cmd[2],#z_error,
							yaw = cmd[3])#angle_error)

		if self.current_height > 0.1:
			self.setpoint_pub.publish(command)

	def cb_update_GSD(self, msg):
		self.GSD = msg.data

	def pid_control(self,x,y,z,angle):
		error = np.array([[x],[y],[z],[angle]])

		curr_time = time()
		dedt = np.array([[0],[0],[0],[0]])
		de = error - self.prev_error
		if self.prev_time != None:
			dt = curr_time - self.prev_time
			if dt != 0:
				dedt = de / dt

			self.int_sum = self.int_sum + error*dt

		self.prev_time = curr_time

		cmd = self.P*error + self.I*self.int_sum + self.D*dedt

		return cmd

def main():
	rospy.init_node("drone_controller")

	controller = Controller()

	# rospy.Rate(20)
	rospy.spin()

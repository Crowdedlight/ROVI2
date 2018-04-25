import rospy
from move_drone_relative.msg import MoveDrone
from markerfinder.msg import MarkerLocation
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Float32
from std_srvs.srv import Trigger
from drone_controller.srv import PID, Setpoint
from math import pi, sqrt, sin, cos
from quaternion import quaternion_to_euler_angle, transform2D
import numpy as np

class Controller:
	def __init__(self):
		self.command_pub = rospy.Publisher("/move_drone_relative/set_relative_pose", MoveDrone, queue_size=10)

		rospy.Subscriber("mavros/local_position/pose", PoseStamped, self.cb_pose_update)
		rospy.Subscriber("markerlocator/markerpose", MarkerLocation, self.cb_marker_update)
		rospy.Subscriber("droneinfo/gsd", Float32, self.cb_GSD_update)

		rospy.Service("drone_controller/new_setpoint", Setpoint, self.new_setpoint)
		rospy.Service("drone_controller/set_PID_constants", PID, self.set_PID)
		rospy.Service("drone_controller/return_to_marker", Trigger, self.return_to_marker)
		rospy.Service("drone_controller/goto_vantage_point", Trigger, self.goto_vantage_point)
		rospy.Service("drone_controller/follow_marker", Trigger, self.follow_marker)
		rospy.Service("drone_controller/land_on_marker", Trigger, self.land_on_marker)
		rospy.Service("drone_controller/cancel_current_cmd", Trigger, self.cancel_current_cmd)

		self.busy = False
		self.follow_camera = False
		self.is_landing = False

		self.GSD = 2.0/800
		self.setpoint = np.array([[0],[0],[2],[180]])
		self.current_pose = np.array([[0],[0],[0],[0]])
		self.marker_quality = 0

		self.P = 0.5
		self.I = 0#.002
		self.D = 0.001

		self.int_sum = np.array([[0],[0],[0],[0]])
		self.prev_error = np.array([[0],[0],[0],[0]])
		self.prev_time = None

	def new_setpoint(self, req):
		if not self.busy:
			self.busy = True
			self.follow_camera = False
			self.is_landing = False
			self.setpoint = np.array([[req.x],[req.y],[req.z],[req.yaw]])

			return True, "New setpoint registered ([{}], [{}], [{}], [{}])".format(req.x,req.y,req.z,req.yaw)

		return False, "Can't execute command. Controller is busy."

	def set_PID(self, req):
		self.P = req.P
		self.I = req.I
		self.D = req.D

		return True, "New PID constants registered (P={}, I={}, D={})".format(self.P,self.I,self.D)

	def return_to_marker(self, req):
		if not self.busy:
			self.busy = True
			self.follow_camera = False
			self.is_landing = False
			self.setpoint = np.array([[0],[0],[2],[180]])

		else:
			return False, "Can't execute command. Controller is busy."

		return True, "Command acknowledged."

	def follow_marker(self, req):
		if not self.busy:
			self.busy = True
			self.follow_camera = True
			self.is_landing = False

		else:
			return False, "Can't execute command. Controller is busy."

		return True, "Command acknowledged."

	def land_on_marker(self, req):
		if not self.busy:
			if self.ready_to_land:
				self.is_landing = True
				return True, "Attempting to land on marker"

			return False, "Can't land. Not above marker yet"

		return False, "Can't execute command. Controller is busy."

	def goto_vantage_point(self, req):
		if not self.busy:
			self.busy = True
			self.follow_camera = False
			self.is_landing = False
			self.setpoint = np.array([[3], [4], [10], [180]])
		else:
			return False, "Can't execute command. Controller is busy."

		return True, "Command acknowledged."

	def cancel_current_cmd(self, req):
		self.setpoint = self.current_pose
		self.busy = False
		self.is_landing = False
		self.follow_camera = False

		return True, "Cancelled current command"

	def cb_pose_update(self, msg):
		x = msg.pose.position.x
		y = msg.pose.position.y
		z = msg.pose.position.z
		_, _, yaw = quaternion_to_euler_angle(msg.pose.orientation)
		self.current_pose = np.array([[x],[y],[z],[yaw]])
		#print(msg)

	def cb_marker_update(self, msg):
		x = msg.x
		y = msg.y
		theta = msg.theta * 180 / pi
		self.marker_quality = msg.quality

		# the camera is not aligned with the drone
		x_error = -y*self.GSD
		y_error = -x*self.GSD
		z_error = 0
		angle_error = 0
		if sqrt(x_error**2 + y_error**2) < 2:
			angle_error = (-theta - 90)

		self.marker_error = np.array([[x_error],[y_error],[z_error],[angle_error]])

	def cb_GSD_update(self, msg):
		self.GSD = msg.data

	def pid_control(self,error):
		curr_time = rospy.get_time()
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

	def run(self):

		error = np.array([[0],[0],[0],[0]])

		if self.follow_camera:# and self.marker_quality > 0.2:
			error = self.marker_error

			# adjust height slowly if landing
			if self.is_landing:
				error[2] -= 0.5

		else:
			# calculate angle and translation from 2D homogenous transformations
			x,y,angle = transform2D(self.current_pose,self.setpoint)
			error = self.setpoint - self.current_pose
			error[0] = x; error[1] = y; error[3] = -angle

		if abs(error[0]) < 0.5 and abs(error[1]) < 0.5 and abs(error[2]) < 0.5 and abs(error[3]) < 0.5 and self.busy:
			self.busy = False

			if self.follow_camera:
				self.ready_to_land = True

				if self.is_landing:
					# keep going
					self.busy = True

				if self.is_landing and self.current_pose[2] < 0.5:
					# stop following marker and land where you are
					self.setpoint = self.current_pose
					# don't actually land
					self.setpoint[2] = 0.4
					self.follow_camera = False
					self.is_landing = False

		cmd = self.pid_control(error)

		command = MoveDrone(x = cmd[0],#x_error,
							y = cmd[1],#y_error,
							z = cmd[2],#z_error,
							yaw = cmd[3])#angle_error)

		self.command_pub.publish(command)

def main():
	rospy.init_node("drone_controller")
	rospy.sleep(1)

	controller = Controller()

	rate = rospy.Rate(50)

	while not rospy.is_shutdown():
		controller.run()
		rate.sleep()

	rospy.loginfo("Shutting down controller node")
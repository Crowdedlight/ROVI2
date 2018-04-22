from math import cos, sin, pi, atan2, asin, degrees, sqrt
from geometry_msgs.msg import PoseStamped, Quaternion
from genpy.message import fill_message_args
import numpy as np

def euler_angle_2_quaternion(R,P,Y):
	cr = cos(R * 0.5)
	sr = sin(R * 0.5)
	cp = cos(P * 0.5)
	sp = sin(P * 0.5)
	cy = cos(Y * 0.5)
	sy = sin(Y * 0.5)

	w = cy * cr * cp + sy * sr * sp
	x = cy * sr * cp - sy * cr * sp
	y = cy * cr * sp + sy * sr * cp
	z = sy * cr * cp - cy * sr * sp

	q = Quaternion()
	fill_message_args(q, [x,y,z,w])

	return q

def quaternion_to_euler_angle(w, x, y, z):
	ysqr = y * y

	t0 = +2.0 * (w * x + y * z)
	t1 = +1.0 - 2.0 * (x * x + ysqr)
	X = degrees(atan2(t0, t1))

	t2 = +2.0 * (w * y - z * x)
	t2 = +1.0 if t2 > +1.0 else t2
	t2 = -1.0 if t2 < -1.0 else t2
	Y = degrees(asin(t2))

	t3 = +2.0 * (w * z + x * y)
	t4 = +1.0 - 2.0 * (ysqr + z * z)
	Z = degrees(atan2(t3, t4))

	return X, Y, Z

def quaternion_mult(q1,q2):
	w = q1.w*q2.w - q1.x*q2.x - q1.y*q2.y - q1.z*q2.z
	x = q1.w*q2.x + q1.x*q2.w + q1.y*q2.z - q1.z*q2.y
	y = q1.w*q2.y + q1.y*q2.w + q1.z*q2.x - q1.x*q2.z
	z = q1.w*q2.z + q1.z*q2.w + q1.x*q2.y - q1.y*q2.x

	q = Quaternion()
	fill_message_args(q, [x,y,z,w])

	return q

def quaternion_to_rot_matrix(q):
	w = q.w
	x = q.x
	y = q.y
	z = q.z

	matrix = np.array([	[1-2*y*y-2*z*z, 2*(x*y-z*w), 2*(x*z+y*w)],
			  			[2*(x*y+z*w), 1-2*x*x-2*z*z, 2*(y*z-x*w)],
			  			[2*(x*z-y*w), 2*(y*z+x*w), 1-2*x*x-2*y*y]])

	return matrix

def posestamped_to_transform(ps, yaw_angle=0):
	w = ps.pose.orientation.w
	x = ps.pose.orientation.x
	y = ps.pose.orientation.y
	z = ps.pose.orientation.z

	X = ps.pose.position.x
	Y = ps.pose.position.y
	Z = ps.pose.position.z

	matrix = np.array([	[1-2*y*y-2*z*z, 2*(x*y-z*w), 2*(x*z+y*w), X],
			  			[2*(x*y+z*w), 1-2*x*x-2*z*z, 2*(y*z-x*w), Y],
			  			[2*(x*z-y*w), 2*(y*z+x*w), 1-2*x*x-2*y*y, Z],
						[0,					0,				0,	  1]])

	return matrix

def transformation_matrix(q, X, Y, Z, yaw):

	delta_q = euler_angle_2_quaternion(0,0,yaw)
	new_q = quaternion_mult(q,delta_q)
	rot = quaternion_to_rot_matrix(new_q)

	matrix = np.array([	[rot[0,0], rot[0,1], rot[0,2], X],
			  			[rot[1,0], rot[1,1], rot[1,2], Y],
			  			[rot[2,0], rot[2,1], rot[2,2], Z],
						[0,	0, 0, 1]])

	return matrix

def matrix_to_posestamped(mat):
	m00 = mat[0, 0]; m01 = mat[0, 1]; m02 = mat[0, 2]
	m10 = mat[1, 0]; m11 = mat[1, 1]; m12 = mat[1, 2]
	m20 = mat[2, 0]; m21 = mat[2, 1]; m22 = mat[2, 2]

	tr = m00 + m11 + m22

	#qw = 0; qx = 0; qy = 0; qz = 0

	if (tr > 0):
		S = sqrt(tr+1.0) * 2 # S=4 * qw
		qw = 0.25 * S
		qx = (m21 - m12) / S
		qy = (m02 - m20) / S
		qz = (m10 - m01) / S
	elif ((m00 > m11) and (m00 > m22)):
		S = sqrt(1.0 + m00 - m11 - m22) * 2 # S=4 * qx
		qw = (m21 - m12) / S
		qx = 0.25 * S
		qy = (m01 + m10) / S
		qz = (m02 + m20) / S
	elif (m11 > m22):
		S = sqrt(1.0 + m11 - m00 - m22) * 2 # S=4 * qy
		qw = (m02 - m20) / S
		qx = (m01 + m10) / S
		qy = 0.25 * S
		qz = (m12 + m21) / S
	else:
		S = sqrt(1.0 + m22 - m00 - m11) * 2 # S=4 * qz
		qw = (m10 - m01) / S
		qx = (m02 + m20) / S
		qy = (m12 + m21) / S
		qz = 0.25 * S

	pose = PoseStamped()
	args = [{'pose': {'position': [mat[0,3],mat[1,3],mat[2,3]], 'orientation': [qx, qy, qz, qw]} }]
	fill_message_args(pose,args)
	print(pose)

	return pose

def perform_yaw(ps, yaw):
	q = euler_angle_2_quaternion(0, 0, yaw)
	delta_pose = PoseStamped()
	args = [{'pose': {'position': [0,0,2], 'orientation': [q.x, q.y, q.z, q.w]} }]
	fill_message_args(delta_pose, args)

	pose = PoseStamped()
	q = quaternion_mult(ps.pose.orientation, delta_pose.pose.orientation)
	# args = [{'pose': {'position': [ps.pose.position.x, ps.pose.position.y, ps.pose.position.z], 'orientation': [q.x, q.y, q.z, q.w]}}]
	# fill_message_args(pose, args)

	return q
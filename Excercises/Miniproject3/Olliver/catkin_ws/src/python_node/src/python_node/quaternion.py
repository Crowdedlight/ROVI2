from math import cos, sin, pi, atan2, asin, degrees
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

	return w, x, y, z

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

	return w, x, y, z

def quaternion_to_rot_matrix(w,x,y,z):
	np.array([[1-2*y*y-2*z*z, 2*(x*y-z*w), 2*(x*z+y*w)],
			  [2*(x*y+z*w), 1-2*x*x-2*z*z, 2*(y*z-x*w)],
			  [2*(x*z-y*w), 2*(y*z+x*w), 1-2*x*x-2*y*y]])
	pass

def posestamped_to_transform(ps):
	pass
##################################################
# In this tutorial we will write a Python module
# that contains a few functions and can be
# called from a Python script or a 
# Python command shell.
#
# usage example:
# ipython
# import tutorial3 as tut
# v = [10, 5, 8]
# theta = 10
# phi = 30
# tut.print_some_results()
#
##################################################

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm, norm

def convert_degree_to_rad(theta):
	return theta*np.pi/180

'''
This function create the cross
product of the identity matrix 
with the normalised rotation axis a, i.e.
the skew-symmetric matrix 
'''
def skew_sym_matrix(axis, theta):
	return expm(np.cross(np.eye(3), axis/norm(axis)*theta) )

'''
this functions rotates a vector
around x axis.
v: the vector
theta: rotation angle in degree
'''
def rotate_x(v, theta):
	a = [1, 0, 0]
	th_rad = convert_degree_to_rad(theta=theta)
	M = skew_sym_matrix(a, theta=th_rad)
	return np.dot(M, v)

def rotate_z(v, phi):
	a = [0, 0, 1]
	phi_rad = convert_degree_to_rad(theta=phi)
	M = skew_sym_matrix(a, theta=phi_rad)
	return np.dot(M, v)

'''
this function outputs the results.
The user has to specify a vector for the function.
The rotation angles are theta (x-axis) and phi (z-axis)
'''
def print_some_results(v, theta, phi):
	rx = rotate_x(v, theta=theta)
	rz = rotate_z(v, phi=phi)
	print('the original vector: ', v)
	print('rotation around x axis: ', rx)
	print('rotation around z axis: ', rz)
	print('cross product of rotated vectors: ', np.cross(rx, rz))



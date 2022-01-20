################################################
# In this tutorial we will rotate a vector v
# around an axis a
#
# example values: 
# v = [10, 8, 2] #  an arbitrary vector
# a = [3, 2, 0] # an arbitrary axis
# theta = np.pi/3 # an arbitrary rotation angle 
# in radian 
#
# usage example:
# python3 tutorial1.py
#
################################################

import numpy as np
from scipy.linalg import expm, norm


'''
This function create the cross
product of the identity matrix 
with the normalised rotation axis a, i.e.
the skew-symmetric matrix 
'''
def skew_sym_matrix(axis, theta):
	return expm(np.cross(np.eye(3), axis/norm(axis)*theta) )

v, a, theta = [10, 8, 2], [3, 2, 0], np.pi/3

M = skew_sym_matrix(axis=a, theta=theta)

print(np.dot(M, v))
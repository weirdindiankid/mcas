# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:34:46 2017

@author: weirdindiankid <Dharmesh Tarapore>
"""

import math

class Vector:

	x = 0.0
	y = 0.0
	z = 0.0

	def __init__(self, x=0.0, y=0.0, z=0.0):
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)

	def magnitude(self):
		"""
			Returns the norm (length, magnitude) of the vector
		"""
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)


	def __add__(self, other):
		"""
			Returns the vector addition of self and other
		"""
		return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

	def __sub__(self, other):
		""" Returns the vector difference of self and other """
		return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

	def __repr__(self):
		return "Vector (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"






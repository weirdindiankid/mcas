# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:44:06 2017

@author: vincentwahl
"""
import Vector

class Plane:
  position = [0.0, 0.0, 0.0]
  velocity = Vector(0.0, 0.0, 0.0, 0.0)
  tail_num = ""
  squawk_code = ""
  planes_in_range = []
    
    
  def __init__(self, position, velocity, tail_num, squawk_code, planes_in_range):
    self.position           = [0.0, 0.0, 0.0]
    self.velocity           = velocity
    self.tail_num           = tail_num
    self.squawk_code        = squawk_code
    self.planes_in_range    = planes_in_range
    
  def update_position(self):
    new_position    = self.position
    new_position[0] += self.velocity.direction[0] * self.velocity.scale
    new_position[1] += self.velocity.direction[1] * self.velocity.scale
    new_position[2] += self.velocity.direction[2] * self.velocity.scale
    self.position = new_position
    
  def update_velocity(self, new_velocity):
    self.velocity = new_velocity
    
  def update_planes_in_range(self):
    print("NYI")
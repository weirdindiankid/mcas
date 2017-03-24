# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:44:06 2017

@author: vincentwahl
"""
import Vector

class Plane:
  position = Vector() 
  velocity = Vector()
  tail_num = ""
  squawk_code = ""

  
  
  def __init__(self, position, velocity, tail_num, squawk_code, planes_in_range):
    self.position           = position
    self.velocity           = velocity
    self.tail_num           = tail_num
    self.squawk_code        = squawk_code
    self.planes_in_range    = planes_in_range
    
  def update_position(self):
    self.position = self.position + self.velocity
    
  def update_velocity(self, new_velocity):
    self.velocity = new_velocity
    
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:44:06 2017

@author: vincentwahl
"""
from Vector import *

class Plane:
  position = Vector(0,0,0) 
  velocity = Vector(0,0,0)
  # In degrees
  course = 0
  speed = 65
  tail_num = ""

  
  
  def __init__(self, position, speed, course, vertical_speed, tail_num):
    self.position           = position
    self.velocity           = Vector(speed * math.cos(course), speed*math.sin(course), vertical_speed)
    self.tail_num           = tail_num
    
  def update_position(self):
    self.position = self.position + self.velocity
    
  def update_velocity(self, new_velocity):
    self.velocity = new_velocity
    
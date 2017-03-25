# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:44:06 2017

@author: vincentwahl
"""
from vector import *

class Plane:

  position = Vector(0,0,0) 
  velocity = Vector(0,0,0)
  # In degrees
  course = 0
  speed = 65
  vertical_speed = 0
  tail_num = ""
  
  
  def __init__(self, position, speed, course, vertical_speed, tail_num):
    self.position           = position
    self.speed              = speed
    self.vertical_speed     = vertical_speed
    self.velocity           = Vector(speed * math.sin(math.radians(course)), speed * math.cosine(math.radians(course)), vertical_speed)
    self.tail_num           = tail_num
    
  def update_position(self):
    self.position = self.position + Vector(self.velocity.x / 3600, self.velocity.y / 3600, self.velocity.z / 3600)
    
  def update_velocity(self, new_velocity):
    self.velocity = new_velocity
    
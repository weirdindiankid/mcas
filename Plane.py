# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:44:06 2017

@author: vincentwahl
"""
import Vector

class Plane:
  position = Vector() 
  velocity = Vector()
  # In degrees
  course = 0
  speed = 65
  tail_num = ""

  
  
  def __init__(self, position, speed=65, course=0, vertical_speed=0, tail_num):
    self.position           = position
    self.velocity           = (speed * math.cosine(course), speed*math.sin(course), vertical_speed)
    self.tail_num           = tail_num
    
  def update_position(self):
    self.position = self.position + self.velocity
    
  def update_velocity(self, new_velocity):
    self.velocity = new_velocity
    
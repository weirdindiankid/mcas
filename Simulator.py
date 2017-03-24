# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:37:38 2017

@author: vincentwahl
"""
import Vector
import Plane
import Random

class Simulator:
  
  #CONSTANTS
  MAP_SIZE = 400
  DELTA_ALTITUDE_RANGE = (-6000, 6000)
  
  planes = []    
  time = 0
  
  def random_spawn_plane(self):
    side = Random.choice(0,1,2,3) #0 = top, then clockwise
    position = Vector()
    
    if side == 0:
      position.x = Random.Random()*MAP_SIZE
      position.y = MAP_SIZE
      position.z = Random.Random()*MAP_SIZE
    
    
    entering = Random.Random()*self.MAP_SIZE[0]

  
  def update_all_planes_positions(self):
    for plane in self.planes:
      plane.update_position()
    return 0
       
    
  def step(self):
    self.update_all_planes_positions()
    self.update_all_planes_velocities()
    self.update_all_planes_in_range_lists()
        
    self.time += 1
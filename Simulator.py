# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:37:38 2017

@author: vincentwahl
"""
import Vector
import Plane

class Simulator:
  
  planes = []
  simulated_map_size = []    
  time = 0
    
  def add_plane(self):
    print("NYI")
    
  def update_all_planes_positions(self):
    for plane in self.planes:
      plane.update_position()
    return 0
        
  def update_all_planes_in_range_lists(self):
    for plane in self.planes:
      plane.update_planes_in_range
    return 0
    
  def update_all_planes_velocities(self):
    print("NYI")
    
  def step(self):
    self.update_all_planes_positions()
    self.update_all_planes_velocities()
    self.update_all_planes_in_range_lists()
        
    self.time += 1
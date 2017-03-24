# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:34:46 2017

@author: vincentwahl
"""

class Vector:
    scale = 1
    direction = [0.0, 0.0, 0.0]

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





























    
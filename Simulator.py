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
  MAP-SIZE_Z = 105600 #feet
  DELTA_ALTITUDE_RANGE = (-2000, 2000)
  
  number_spawned_planes = 0
  planes = []    
  time = 0
  
  def random_spawn_plane(self):
    #position    
    side = Random.choice(0,1,2,3) #0 = top, then clockwise
    position = Vector()
    rand1 = Random.Random()
    rand2 = Random.Random()
    
    if side == 0:
      position.x = rand1* MAP_SIZE
      position.y =        MAP_SIZE
      position.z = rand2* MAP_SIZE
    elif (side == 1):
      position.x =        MAP_SIZE
      position.y = rand1* MAP_SIZE
      position.z = rand2* MAP_SIZE
    elif (side == 2):
      position.x = rand1* MAP_SIZE
      position.y = 0
      position.z = rand2* MAP_SIZE
    elif (side == 3):
      position.x =        MAP_SIZE
      position.y = rand1* MAP_SIZE
      position.z = rand2* MAP_SIZE
    
    #speed
    speed = int(Random.normal(300, 50))
    if speed < 65:
      speed = 65
    elif speed > 550:
      speed = 550
    
<<<<<<< HEAD
    #course
    course = Random.randint(0,360)
    
    #vertical_speed
    vertical_speed = Random.randint(-500, 500, 1000, -1000, 0)
    
    #tail number
    tail_num = str(number_spawned_planes)
    

    plane = Plane(position, speed, course, vertical_speed, tail_num, )
    
    planes.append(plane)
    
    number_spawned_planes += 1

=======
    entering = Random.Random()*self.MAP_SIZE[0]
>>>>>>> 6be1ab386590cfe80dcca732b9945510fed72ba5

  
  def update_all_planes_positions(self):
    for plane in self.planes:
      plane.update_position()
<<<<<<< HEAD
  

=======
    return 0
       
>>>>>>> 6be1ab386590cfe80dcca732b9945510fed72ba5
    
  def step(self):
    self.update_all_planes_positions()
    #self.update_all_planes_velocities()
    self.update_all_planes_in_range_lists()
        
    self.time += 1











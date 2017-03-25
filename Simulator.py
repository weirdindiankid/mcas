# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:37:38 2017

@author: vincentwahl
"""
from Vector import *
from Plane import *
import numpy
import random as Random

class Simulator:
  
  #CONSTANTS
  MAP_SIZE = 400

  # Spawn Int.
  SPAWN_INTERVAL = 20

  # NM Foot conversion for position checks
  SEPARATION_THRESHOLD_MAGNITUDE = 0.493736599
  COLLISION_THRESHOLD_MAGNITUDE = 0.0493736599
  #LATERAL_SEPARATION_THRESHOLD = 0.3291577 # 2000 feet
  #VERTICAL_SEPARATION_THRESHOLD = 0.164579  # 1000 feet

  
  number_spawned_planes = 0
  planes = []    
  time = 0
  
  def random_spawn_plane(self):
    #position    
    side = Random.choice([0,1,2,3]) #0 = top, then clockwise
    position = Vector()
    rand1 = Random.random()
    rand2 = Random.random()
    
    if side == 0:
      position.x = rand1 * self.MAP_SIZE
      position.y =         self.MAP_SIZE
      position.z = rand2 * self.MAP_SIZE
    elif (side == 1):
      position.x =         self.MAP_SIZE
      position.y = rand1 * self.MAP_SIZE
      position.z = rand2 * self.MAP_SIZE
    elif (side == 2):
      position.x = rand1 * self.MAP_SIZE
      position.y = 0
      position.z = rand2 * self.MAP_SIZE
    elif (side == 3):
      position.x =         self.MAP_SIZE
      position.y = rand1 * self.MAP_SIZE
      position.z = rand2 * self.MAP_SIZE
    
    #speed
    speed = int(numpy.random.normal(300, 50))
    if speed < 65:
      speed = 65
    elif speed > 550:
      speed = 550
    
    #course
    course = Random.randint(0,360)
    
    #vertical_speed
    vertical_speed = Random.choice([-4.93, 4.93, 9.87, -9.87, 0])
    
    #tail number
    tail_num = str(self.number_spawned_planes)
    

    plane = Plane(position, speed, course, vertical_speed, tail_num)
    
    self.planes.append(plane)
    
    self.number_spawned_planes += 1


  def distance_between_planes(self):
    distanceDict = {}
    collisionDict = {}
    for i in range(len(self.planes)):
      for j in range(i+1, len(self.planes)):
        plane_dist = self.planes[i].position - self.planes[j].position
        plane_dist = plane_dist.magnitude()

        # Actual thresholds in constants
        if plane_dist < self.SEPARATION_THRESHOLD_MAGNITUDE:
          if plane_dist < self.COLLISION_THRESHOLD_MAGNITUDE:
            collisionDict[ str(self.planes[i].tail_num) + "--" + str(self.planes[i+1].tail_num) ] = plane_dist
          distanceDict[ str(self.planes[i].tail_num) + "--" + str(self.planes[i+1].tail_num) ] = plane_dist
    print(distanceDict)
    return (distanceDict, collisionDict)


  
  def update_all_planes_positions(self):
    for plane in self.planes:
      plane.update_position()

    
  def step(self):

    self.update_all_planes_positions()
    #self.update_all_planes_in_range_lists()
    if self.time % self.SPAWN_INTERVAL == 0:
      self.random_spawn_plane()

    self.distance_between_planes()
    print("Num planes: " + str(len(self.planes)))
    self.time += 1

a = Simulator()
for i in range(1000):
  a.step()
  










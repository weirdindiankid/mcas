# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:37:38 2017

@author: vincentwahl
"""

from vector import *
from Plane import *
import numpy as np
import sys
import random as Random



class Simulator:
  
  #CONSTANTS
  MAP_SIZE = 15

  # Spawn Int.
  SPAWN_INTERVAL = 20

  # NM Foot conversion for position checks
  SEPARATION_THRESHOLD_MAGNITUDE = 0.493736599
  COLLISION_THRESHOLD_MAGNITUDE = 0.0493736599
  


  
  number_spawned_planes = 0
  planes = []    
  simTime = 0
  number_of_RIP = 0
  
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
      position.x =         0
      position.y = rand1 * self.MAP_SIZE
      position.z = rand2 * self.MAP_SIZE
    
    #speed
    speed = int(np.random.normal(300, 50))
    
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

    #print("Plane " + plane.tail_num + ": position: " + str(plane.position) + " speed: " + str(plane.speed) + " vs: " + str(plane.vertical_speed))

    
    self.planes.append(plane)
    
    self.number_spawned_planes += 1


  def delete_planes(self):
    '''
      Deletes planes when they've gone too far (no pun intended).
    '''
    for plane in self.planes:
      if (0 > plane.position.x < self.MAP_SIZE) or (0 > plane.position.y < self.MAP_SIZE) or (0 > plane.position.y < self.MAP_SIZE):
        self.planes.remove(plane)


  def distance_between_planes(self):
    distanceDict = {}
    collisionDict = {}
    for i in range(len(self.planes)):
      for j in range(i+1, len(self.planes)):

        plane_dist = self.planes[i].position - self.planes[j].position
        plane_dist = plane_dist.magnitude()

        #print(plane_dist)

        # Actual thresholds in constants
        if plane_dist < (self.SEPARATION_THRESHOLD_MAGNITUDE):
          if plane_dist < self.COLLISION_THRESHOLD_MAGNITUDE:
            collisionDict[ str(self.planes[i].tail_num) + "--" + str(self.planes[i+1].tail_num) ] = plane_dist
          distanceDict[ str(self.planes[i].tail_num) + "--" + str(self.planes[i+1].tail_num) ] = plane_dist
          #print("Inappropriate separation: " + str(self.planes[i].tail_num) + "--" + str(self.planes[i+1].tail_num))
          self.number_of_RIP += 1
          #sys.exit(0)

    # print(distanceDict)
    return (distanceDict, collisionDict)


  
  def update_all_planes_positions(self):
    for plane in self.planes:
      plane.update_position()

    
  def step(self):

    self.update_all_planes_positions()
    #self.update_all_planes_in_range_lists()
    if self.simTime % self.SPAWN_INTERVAL == 0:
      self.random_spawn_plane()
    self.distance_between_planes()
    #print("Num planes: " + str(len(self.planes)))
    self.delete_planes()
    self.simTime += 1




#SEEEEDS
a = Simulator()
for i in range(5000):
  a.step()
print("# of RIPs: "+ str(a.number_of_RIP))
print("# of planes spawned: " + str(a.number_spawned_planes))
print("# of planes at the end: " + str(len(a.planes)))




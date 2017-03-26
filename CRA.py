# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 14:20:58 2017

@author: vincentwahl
"""

#Colission Resolution Advisory

#in [planes]
#out [(tailNum, altitude change)]

import numpy as np
from Plane import *
from Vector import *
import math

class CRA():


def XYRelativeDistanceDecreasingOrConstant(A, B):
  v = [B.velocity.x-A.velocity.x, B.velocity.y-A.velocity.y]
  d = [B.position.x-A.position.x, B.position.y-A.position.y]
  
  dot = np.dot(v,d)
  dot = np.linalg.norm(dot)
    
  if (dot <= 0):
    return True
  else:
    return False


def riskGraph(planes, riscFactor):
  riskGraph =[]
  for A in planes:
    temp = []
    for B in planes:
      if XYRelativeDistanceDecreasingOrConstant(A,B):
        d = [B.position.x-A.position.x, B.position.y-A.position.y]
        if np.linalg.norm(d) < riscFactor:
          temp.append(B)
    riskGraph.append(temp)
  return riskGraph
    
  

  
  
  
  
#  def XYCollissionDetection(plane1, plane2):
#    print("A: velocity= " + str(plane1.velocity) + ", position: " + str(plane1.position))
#    print("B: velocity= " + str(plane2.velocity) + ", position: " + str(plane2.position))
#    velocityMatrix = np.matrix([[plane1.velocity.x, -plane2.velocity.x],
#                                [plane1.velocity.y, -plane2.velocity.y]])
#    
#    relativePositionVector = [[plane2.position.x - plane1.position.x],
#                              [plane2.position.y - plane1.position.y]]
#    
#    t = np.linalg.solve(velocityMatrix, relativePositionVector)
#    
#    if t[0][0] == t[1][0]:
#      print("collision")
#    else:
#      print("no colission")
  
  
  
  
  
  #position, speed, course, vertical_speed, tail_num
  
  A = Plane(Vector(0,0,0), 0, 0, 0, "A")
  A.velocity.x = 1
  A.velocity.y = 1
  A.position.x = 1
  A.position.y = 1
  
  B = Plane(Vector(0,0,0), 0, 0, 0, "A")
  B.velocity.x = 2
  B.velocity.y = 2
  B.position.x = 0
  B.position.y = 0
  
  XYCollissionDetection(A,B)
  
  











# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 09:33:02 2022

@author: emmid
"""
import re

class MoveShip():
    
    def __init__(self):
        self.directionList = ['E', 'S', 'W', 'N']
        self.currentOff = 0
        self.direction = 'E'
        self.ship = Ship()
        self.waypoint = Waypoint()
        print('init')
        
    def calculateManhattan(self, string):
        print('calculate')
        val = re.split('(\d+)', string)
        intVal = int(val[1])
        
        if (val[0] == 'L' or val[0] == 'R'):
            self.getDirectionAndWaypoint(val[0], intVal)
            
        elif (val[0] == 'E'):
            self.waypoint.x += intVal
        
        elif (val[0] == 'S'):
            self.waypoint.y += -abs(intVal)
            
        elif (val[0] == 'W'):
            self.waypoint.x += -abs(intVal)
            
        elif (val[0] == 'N'):
            self.waypoint.y += intVal
            
        elif (val[0] == 'F'):
            valX = intVal * self.waypoint.x
            valY = intVal * self.waypoint.y

            self.ship.eastWestDistance += valX
            self.ship.northSouthDistance += valY
                
        return abs(self.ship.eastWestDistance) + abs(self.ship.northSouthDistance)

        
        
    def getDirectionAndWaypoint(self, direction, degree):
        offset = degree / 90
        previousWaypointX = self.waypoint.x
        previousWaypointY = self.waypoint.y
        
        if (direction == 'R'):            
            self.currentOff += int(offset)
            self.currentOff = self.currentOff % 4
            self.direction = self.directionList[self.currentOff]            
            print ('turn right')
                
        elif (direction == 'L'):
            self.currentOff -= int(offset)
            self.currentOff = self.currentOff % 4
            self.direction = self.directionList[self.currentOff]
            print ('turn left')            
        
            
        if self.currentOff == 1:
            self.waypoint.x = previousWaypointY
            self.waypoint.y = -abs(previousWaypointX)
        elif self.currentOff == 2:
            self.waypoint.x = -abs(previousWaypointX)
            self.waypoint.y = -abs(previousWaypointY)
        elif self.currentOff == 3:
            self.waypoint.x = -abs(previousWaypointY)
            self.waypoint.y = previousWaypointX
        
    def run(self):
        print('run')
        with open('data.txt', 'r') as file:
            data = file.read().splitlines()
                
        for line in data:
            manhattanDis = self.calculateManhattan(line)
            print(manhattanDis)
        
class Ship():
    def __init__(self):
        self.eastWestDistance = 0
        self.northSouthDistance = 0
        
class Waypoint():
    def __init__(self):
        self.x = 10
        self.y = 1
        print(self.x)
        print(self.y)
        
        
if __name__ == '__main__':
    MoveShip().run()
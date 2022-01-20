# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 10:02:45 2022

@author: emmid
"""
import re

class Application():
    def __init__(self):
        self.directionList = ['E', 'S', 'W', 'N']
        self.currentOff = 0
        self.direction = 'E'
        self.eastDistance = 0
        self.westDistance = 0
        self.northDistance = 0
        self.southDistance = 0
        self.northSouth = 0
        self.eastwest = 0
        print('init')
        
    def calculateManhattan(self, string):
        print('calculate')

        val = re.split('(\d+)', string)
        intVal = int(val[1])
        
        if (val[0] == 'L' or val[0] == 'R'):
            self.getDirection(val[0], intVal)

        elif (val[0] == 'F'):

            if (self.direction == 'E'):
                self.eastDistance += intVal
            elif (self.direction == 'S'):
                self.southDistance += intVal
            elif (self.direction == 'W'):
                self.westDistance += intVal
            elif (self.direction == 'N'):
                self.northDistance += intVal
        
        elif (val[0] == 'E'):
            self.eastDistance += intVal
        
        elif (val[0] == 'S'):
            self.southDistance += intVal
            
        elif (val[0] == 'W'):
            self.westDistance += intVal
            
        elif (val[0] == 'N'):
            self.northDistance += intVal
            
        self.northSouth = abs(self.northDistance - self.southDistance)
        self.eastwest = abs(self.eastDistance - self.westDistance)
        
        return self.northSouth + self.eastwest
                
        
        
    def getDirection(self, direction, degree):
        offset = degree / 90
        
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
                
        
    
    def run(self):
        print('run')
        with open('data.txt', 'r') as file:
            data = file.read().splitlines()
                
        for line in data:
            manhattanDis = self.calculateManhattan(line)
            print(manhattanDis)
    
if __name__ == '__main__':
    Application().run()
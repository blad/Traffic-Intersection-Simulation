from __future__ import division
from visual import *
'''
  This Script Requires that VisualPython be installed in order to 
  run. To Download Visual Python visit: http://www.vpython.org/
'''

'''Configurations'''
dt = 1/30
dr = dt * 3
carLength = 3
lineColor = color.white
road1Color = color.gray(0.4)
road2Color = road1Color
roadLinesColor = color.gray(0.9)
roadStopPoint = 3+carLength/2

class CanPass(object):
    def __init__(self):
        self.canPass = False
    
def main():    
    scene.up = vector(0,1,1)
    scene.forward = vector(0,2,-1)
    scene.scale = vector(.02,.02,.02)
    '''Static Objects'''
    road1 = box(pos=(0,0,-3), length=6, height=150, width=.5, color=road1Color)
    road2 = box(pos=(0,0,-3), length=150, height=6, width=.5, color=road2Color)
    stopLineRoad1     = box(pos=(0,3,-2.9), length=6, height=0.5, width=.5, color=lineColor)
    passCompleteRoad1 = box(pos=(0,-3,-2.9), length=6, height=0.5, width=.5, color=lineColor)
    stopLineRoad2     = box(pos=(3,0,-2.9), length=.5, height=6, width=.5, color=lineColor)
    passCompleteRoad2 = box(pos=(-3,0,-2.9), length=.5, height=6, width=.5, color=lineColor)
    for i in range(15):
        ''' Top Series of Road Lines'''
        box(pos=(0,(i*5)+6,-2.9), length=.5, height=3, width=.5, color=roadLinesColor)
        ''' Bottom Series of Road Lines'''
        box(pos=(0,-(i*5)-6,-2.9), length=.5, height=3, width=.5, color=roadLinesColor)
        ''' Right Series of Road Lines'''
        box(pos=((i*5)+6,0,-2.9), length=3, height=.5, width=.5, color=roadLinesColor)
        ''' Right Series of Road Lines'''
        box(pos=(-(i*5)-6,0,-2.9), length=3, height=.5, width=.5, color=roadLinesColor)
    
    '''Animation Objects'''
    vehiclesRoad1 = []
    vehiclesRoad1.append((0, box(pos=(0, roadStopPoint + 0,-2.1), height=carLength, length=1, width=1,  color=color.orange), CanPass()))
    vehiclesRoad1.append((4, box(pos=(0, roadStopPoint + 12 ,-2.1), height=carLength, length=1, width=1,  color=color.orange), CanPass()))
    vehiclesRoad1.append((10, box(pos=(0,roadStopPoint + 30,-2.1), height=carLength, length=1, width=1,  color=color.orange), CanPass()))
    vehiclesRoad1.append((15, box(pos=(0,roadStopPoint + 45,-2.1), height=carLength, length=1, width=1,  color=color.orange), CanPass()))
    vehiclesRoad1.append((21, box(pos=(0,roadStopPoint + 63,-2.1), height=carLength, length=1, width=1,  color=color.orange), CanPass()))
    
    vehiclesRoad2 = []
    vehiclesRoad2.append((2, box(pos=(roadStopPoint + 6,0,-2.1), height=1, length=carLength, width=1,  color=color.blue), CanPass()))
    vehiclesRoad2.append((8, box(pos=(roadStopPoint + 24,0,-2.1), height=1, length=carLength, width=1,  color=color.blue), CanPass()))
    vehiclesRoad2.append((15, box(pos=(roadStopPoint + 45,0,-2.1), height=1, length=carLength, width=1,  color=color.blue), CanPass()))
    vehiclesRoad2.append((22, box(pos=(roadStopPoint + 66,0,-2.1), height=1, length=carLength, width=1,  color=color.blue), CanPass()))
    
    '''Main Animation Loop'''
    while True :
        rate(1/dt)
        ''' Update Position of Vehicles in Road 1 '''
        for i in range (len(vehiclesRoad1)) :
            if (vehiclesRoad1[i][1].y < roadStopPoint and vehiclesRoad1[i][2].canPass):
                vehiclesRoad1[i][1].y = vehiclesRoad1[i][1].y - dr
            elif (i > 0 and (vehiclesRoad1[i][1].y > (vehiclesRoad1[(i-1)][1].y + carLength + .5))):
                vehiclesRoad1[i][1].y = vehiclesRoad1[i][1].y - dr

        ''' Update Position of Vehicles in Road 2 '''
        for i in range (len(vehiclesRoad2)) :
            if (vehiclesRoad2[i][1].x > roadStopPoint and vehiclesRoad2[i][2].canPass):
                vehiclesRoad2[i][1].x = vehiclesRoad2[i][1].x - dr
            elif (i > 0 and (vehiclesRoad2[i][1].x > (vehiclesRoad2[(i-1)][1].x + carLength + .5))):
                vehiclesRoad2[i][1].x = vehiclesRoad2[i][1].x - dr
            elif (i == 0 and vehiclesRoad2[i][1].x > roadStopPoint):
                vehiclesRoad2[i][1].x = vehiclesRoad2[i][1].x - dr


if __name__ == "__main__" :
    main()

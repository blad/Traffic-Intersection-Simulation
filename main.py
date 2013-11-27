from __future__ import division
from visual import *
'''
  This Script Requires that VisualPython be installed in order to 
  run. To Download Visual Python visit: http://www.vpython.org/
'''
def main():
    '''Configurations'''
    yLimitBottom = 0
    yLimitTop = 50
    dt = 1/30
    dy = dt * 30
    lineColor = color.white
    road1Color = color.gray(0.4)
    road2Color = road1Color
    roadLinesColor = color.gray(0.9)
    
    '''Static Objects'''
    road1 = box(pos=(0,0,-3), length=6, height=100, width=.5, color=road1Color)
    road2 = box(pos=(0,0,-3), length=100, height=6, width=.5, color=road2Color)
    stopLineRoad1     = box(pos=(0,3,-2.9), length=6, height=0.5, width=.5, color=lineColor)
    passCompleteRoad1 = box(pos=(0,-3,-2.9), length=6, height=0.5, width=.5, color=lineColor)
    stopLineRoad2     = box(pos=(3,0,-2.9), length=.5, height=6, width=.5, color=lineColor)
    passCompleteRoad2 = box(pos=(-3,0,-2.9), length=.5, height=6, width=.5, color=lineColor)
    for i in range(9):
        ''' Top Series of Road Lines'''
        box(pos=(0,(i*5)+6,-2.9), length=.5, height=3, width=.5, color=roadLinesColor)
        ''' Bottom Series of Road Lines'''
        box(pos=(0,-(i*5)-6,-2.9), length=.5, height=3, width=.5, color=roadLinesColor)
        ''' Right Series of Road Lines'''
        box(pos=((i*5)+6,0,-2.9), length=3, height=.5, width=.5, color=roadLinesColor)
        ''' Right Series of Road Lines'''
        box(pos=(-(i*5)-6,0,-2.9), length=3, height=.5, width=.5, color=roadLinesColor)
    
    '''Animation Objects'''
    a = box(pos=(0,yLimitTop-5,0), height=5, length=2, width=2,  color=color.orange)
    
    '''Main Animation Loop'''
    while True :
        rate(1/dt)
        if ((a.y-a.height/2) < -yLimitTop or (a.y+a.height/2) > yLimitTop):
            dy = dy * (-1)
        a.y = a.y + dy
        


if __name__ == "__main__" :
    main()

import pygame
import math
import numpy
import random
import pandas


def distanceFormula(thing1, thing2):
    return math.sqrt((thing1.x-thing2.x)**2 + (thing1.y-thing2.y)**2)


class Spot:  # So you can put it in the distance formula
    def __init__(self, x, y, rad=0):
        self.x = x
        self.y = y
        self.rad = rad


class vWall:
    def __init__(self, x, y1, y2, direct, flag=1):
        self.x = x
        self.top = y1
        self.bot = y2
        self.dir = direct
        self.topSpot = Spot(x, y1)
        self.botSpot = Spot(x, y2)
        self.start = (x, y1)
        self.end = (x, y2)
        self.mid = (x, .5 * (y1 + y2))
        self.flag = flag
        self.dpoint = (x + (20+(30*flag))*direct, .5 * (y1 + y2))

    def withinY(self, thing):
        if self.top <= thing.y <= self.bot:
            return True
        elif distanceFormula(thing, self.topSpot) <= thing.rad:
            return True
        elif distanceFormula(thing, self.botSpot) <= thing.rad:
            return True
        else:
            return False

    def isTouching(self, thing):
        if self.dir == 1:
            if self.x - 5 - (20*self.flag) <= thing.x - thing.rad <= self.x and self.withinY(thing):
                thing.xV = abs(thing.xV)
        else:
            if self.x + 5 + (20*self.flag) >= thing.x + thing.rad >= self.x and self.withinY(thing):
                thing.xV = -abs(thing.xV)


class hWall:
    def __init__(self, y, x1, x2, direct, flag=1):
        self.y = y
        self.left = x1
        self.right = x2
        self.dir = direct  # 1 or -1
        self.leftSpot = Spot(x1, y)
        self.rightSpot = Spot(x2, y)
        self.start = (x1, y)
        self.end = (x2, y)
        self.mid = (.5*(x1+x2), y)
        self.flag = flag
        self.dpoint = (.5*(x1+x2), y + (20+(30*flag))*direct)

    def withinX(self, thing):
        if self.left <= thing.x <= self.right:
            return True
        elif distanceFormula(thing, self.leftSpot) <= thing.rad:
            return True
        elif distanceFormula(thing, self.rightSpot) <= thing.rad:
            return True
        else:
            return False

    def isTouching(self, thing):
        if self.dir == 1:
            if self.y - 5 - (20*self.flag) <= thing.y - thing.rad <= self.y and self.withinX(thing):
                thing.yV = abs(thing.yV)
        else:
            if self.y + 5 + (20*self.flag) >= thing.y + thing.rad >= self.y and self.withinX(thing):
                thing.yV = -abs(thing.yV)


split = 10  # Milliseconds
gameTime = 60  # seconds
gameTime *= 1000  # Milliseconds
kickoffDelay = 1000
accel = .1
decel = .02
blackC = (0, 0, 0)
whiteC = (255, 255, 255)
purpleC = (48, 44, 143)
orangeC = (173, 86, 5)
rosterSize = int(input('Roster Size? (1, 2, 3)'))
if rosterSize not in [1, 2, 3]:
    raise ValueError('You dumb dumb')
seasonLength = int(input('How many round robins in regular season (I\'d say like 1 maybe 2)'))
winX, winY = 1100 + 100*rosterSize, 670 + 30*rosterSize
goalTop = winY*.5 - 150
goalBot = winY*.5 + 150
goalBack = winX*.1
goalFront = winX*.15
startSpots = [None, [(.2, .5)], [(.2, .3), (.15, .75)], [(.3, .3), (.25, .75), (.2, .5)]]
walls = [vWall(0, 0, winY, 1), vWall(winX, 0, winY, -1), hWall(0, 0, winX, 1), hWall(winY, 0, winX, -1),
         hWall(goalTop, goalBack, goalFront, -1), hWall(goalBot, goalBack, goalFront, 1),
         #hWall(goalTop, goalBack, goalFront, 1, flag=0), hWall(goalBot, goalBack, goalFront, -1, flag=0),
         vWall(goalBack, goalTop, goalBot, -1), vWall(goalBack + 30, goalTop, goalBot, 1, flag=0),
         hWall(goalTop, winX-goalFront, winX-goalBack, -1), hWall(goalBot, winX-goalFront, winX-goalBack, 1),
         #hWall(goalTop, winX-goalFront, winX-goalBack, 1, flag=0), hWall(goalBot, winX-goalFront, winX-goalBack, -1, flag=0),
         vWall(winX-goalBack, goalTop, goalBot, 1), vWall(winX-goalBack - 30, goalTop, goalBot, -1, flag=0)]


# Unit Circle is clockwise


def clamp(x, lo, hi):
    if x > hi:
        x = hi
    if x < lo:
        x = lo
    return x


def pythag(x, y):
    return math.sqrt(x**2 + y**2)

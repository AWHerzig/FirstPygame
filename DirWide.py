import pygame
import math
import numpy
import random
import pandas

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
seasonLength = int(input('How many round robins in regular season (I\'d say like 1 maybe 2'))
winX, winY = 900 + 100*rosterSize, 670 + 30*rosterSize
goalTop = winY*.5 - 100
goalBot = winY*.5 + 100
startSpots = [None, [(.1, .5)], [(.2, .3), (.15, .75)], [(.2, .3), (.15, .75), (.1, .5)]]


# Unit Circle is clockwise


def distanceFormula(thing1, thing2):
    return math.sqrt((thing1.x-thing2.x)**2 + (thing1.y-thing2.y)**2)


def clamp(x, lo, hi):
    if x > hi:
        x = hi
    if x < lo:
        x = lo
    return x


def pythag(x, y):
    return math.sqrt(x**2 + y**2)

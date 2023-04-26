import random
import math
from DirWide import *
import names


class Team:
    def __init__(self, name, ABR, home=purpleC, away=orangeC):
        self.name = name
        self.ABR = ABR
        self.discs = []
        for i in range(rosterSize):
            self.discs.append(Disc(ABR, pos=i+1))
        self.side = 0
        self.speed = 0
        self.power = 0
        for i in self.discs:
            self.speed += i.speed
            self.power += i.pow
        self.homeStrip = home
        self.awayStrip = away
        self.wins = 0
        self.smallWins = 0
        self.smallLoss = 0
        self.bigWins = 0
        self.bigLoss = 0
        self.pF = 0
        self.pA = 0
        self.seed = 0
        self.confWinner = 0

    def __str__(self):
        if self.seed > 0:
            return f'{self.seed}. {self.name} {self.speed} {self.power}'
        else:
            return f'{self.name} {self.speed} {self.power}'

    def containsControlled(self):
        for i in self.discs:
            if i.controlled:
                return True
        return False


class Disc:
    def __init__(self, abr='N/A', pos=1, cont=False):
        self.name = names.get_full_name()
        while len(self.name) != 15:
            if len(self.name) > 15:
                self.name = names.get_full_name()
            else:
                self.name = self.name + ' '
        self.team = abr
        self.side = 0
        self.x = 0
        self.y = 0
        self.startX = 0
        self.startY = 0
        self.color = (0, 0, 0)
        self.rad = 40
        self.pow = random.randrange(3, 10)
        self.speed = random.randrange(3, 10)
        self.xV = 0
        self.yV = 0
        self.target = 0
        self.controlled = cont
        self.pos = pos
        # STATS
        self.goals = 0
        self.ownGoals = 0

    def inRangeOf(self, thing):
        if distanceFormula(self, thing) <= self.rad+thing.rad:  # hit
            return True
        else:
            return False

    def canCover(self, spot, splits):
        xDiff = spot.x - self.x
        yDiff = spot.y - self.y
        angle = math.atan(yDiff / xDiff) if xDiff != 0 else math.pi / 4
        angle += math.pi / 4 if xDiff < 0 else 0
        mag = pythag(xDiff, yDiff) - 45
        if mag/self.speed <= splits:
            return True
        else:
            return False

    def __str__(self):
        return self.name

    def statline(self):
        return f'{self.team} {self.name} {self.goals} {self.ownGoals}'


class Ball:
    def __init__(self, x=winX*.5, y=winY*.5, color=whiteC):
        self.x = x
        self.y = y
        self.startX = x
        self.startY = y
        self.xV = 0
        self.yV = 0
        self.dir = 0
        self.color = color
        self.rad = 5
        self.controlled = False



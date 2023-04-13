import numpy
import pygame
import math
from DirWide import *
from Objects import *
from MovementDec import *


def reset(things, spot=0):
    for i in things:
        i.x = i.startX
        i.y = i.startY
        i.xV = 0
        i.yV = 0
        if isinstance(i, Ball):
            side = spot if spot != 0 else random.choice([1, -1])
            i.x = numpy.random.normal(winX*.5 + (side*winX*.2), winX*.1)
            i.y = numpy.random.normal(.5*winY, .1*winY)


def game(left, right, title='', watch=False):
    random.shuffle(left.discs)
    for i in left.discs:
        i.pos = left.discs.index(i) + 1
    random.shuffle(right.discs)
    for i in right.discs:
        i.pos = right.discs.index(i) + 1
    if left.containsControlled() or right.containsControlled() or watch:
        userGame(left, right, user=True, title=title)
    else:
        userGame(left, right, user=False, title=title)


def userGame(left, right, title='', user=False):
    if user:
        dud = input('game is gonna start now')
        pygame.init()
        out = pygame.display.set_mode((winX, winY))
        pygame.display.set_caption(f'{left.ABR} v {right.ABR}; '+title)
    ball = Ball()
    left.side = -1
    right.side = 1
    for i in left.discs:
        i.color = left.homeStrip
        i.side = -1
        (i.startX, i.startY) = startSpots[rosterSize][i.pos-1]
        i.startX *= winX
        i.startY *= winY
    for i in right.discs:
        i.color = right.awayStrip
        i.side = 1
        (i.startX, i.startY) = startSpots[rosterSize][i.pos-1]
        i.startX = (1-i.startX) * winX
        i.startY = (1-i.startY) * winY
    discs = left.discs + right.discs
    things = discs + [ball]
    if user:
        font = pygame.font.Font('freesansbold.ttf', 32)
    time = gameTime
    leftScore = 0
    rightScore = 0
    barrierCrosses = 0
    timeSinceKick = 0
    comTarget = (0, 0)
    lastTouched = None
    kill = False
    reset(things)
    while (time > 0 or leftScore == rightScore) and not kill:
        hits = False
        if user:
            pygame.time.delay(split)
        if time == 0:
            reset(things)
            timeSinceKick = 0
            barrierCrosses = 0
        time -= split
        timeSinceKick += split
        outTime = round(time / 1000, 1) if time >= 0 else 'OT'
        if user:
            text = font.render(f'{leftScore} {outTime} {rightScore}', True, whiteC)
            textL = font.render(f'{left} ({left.wins})', True, whiteC)
            textR = font.render(f'{right} ({right.wins})', True, whiteC)
            textRect = text.get_rect()
            textRect.center = (winX // 2, 50)
            textRectL = textL.get_rect()
            textRectL.center = (winX*.2, 50)
            textRectR = textR.get_rect()
            textRectR.center = (winX * .8, 50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    kill = True
        for item in discs:
            if item.inRangeOf(ball) and not hits:  # Does it hit the ball
                for item2 in discs:
                    if item != item2 and item2.inRangeOf(ball):
                        hits = True
                        lastTouched = item2
                        xDiff = (ball.x - item.x) + (ball.x - item2.x)
                        yDiff = (ball.y - item.y) + (ball.y - item2.y)
                        angle = math.atan(yDiff / xDiff) if xDiff != 0 else math.pi / 4
                        angle = angle + (math.pi if xDiff < 0 else 0)
                        veloMag = pythag(item.xV + item2.xV, item.yV + item2.yV)  # No idea if this'll work
                        veloDir = math.atan(item.yV+item2.yV / item.xV+item2.xV) if item.xV != 0 else math.pi / 4
                        veloDir = veloDir + (math.pi if item.xV+item2.xV < 0 else 0)
                        ballVelo = abs(veloMag * math.cos(veloDir - angle)) + (item.pow + item2.pow)
                        ball.xV = ballVelo * math.cos(angle)
                        ball.yV = ballVelo * math.sin(angle)
                if not hits:
                    lastTouched = item
                    xDiff = ball.x - item.x
                    yDiff = ball.y - item.y
                    angle = math.atan(yDiff / xDiff) if xDiff != 0 else math.pi / 4
                    angle = angle + (math.pi if xDiff < 0 else 0)
                    veloMag = math.sqrt(item.xV ** 2 + item.yV ** 2)
                    veloDir = math.atan(item.yV / item.xV) if item.xV != 0 else math.pi / 4
                    veloDir = veloDir + (math.pi if item.xV < 0 else 0)
                    ballVelo = abs(veloMag*math.cos(veloDir-angle)) + item.pow
                    if ball.rad >= ball.x or ball.x + ball.rad >= winX or ball.rad >= ball.y or ball.y + ball.rad >= winY:
                        ballVelo += 6
                        if ball.rad >= ball.x:
                            angle += math.pi/2 if item.yV < 0 else -math.pi/2
                        elif ball.x + ball.rad >= winX:
                            angle += math.pi / 2 if item.yV > 0 else -math.pi / 2
                        elif ball.rad >= ball.y:
                            angle += math.pi / 2 if item.xV > 0 else -math.pi / 2
                        else:
                            angle += math.pi / 2 if item.xV < 0 else -math.pi / 2
                    ball.xV = ballVelo * math.cos(angle)
                    ball.yV = ballVelo * math.sin(angle)
                    #if xDiff * ball.xV < 0 or yDiff * ball.yV < 0:
                        #print('bruhhhh')
            for target in discs:  # Does it hit another disc
                if item != target and item.inRangeOf(target):
                    velo = item.pow / 2
                    xDiff = target.x - item.x
                    yDiff = target.y - item.y
                    if xDiff != 0:
                        angle = math.atan(yDiff / xDiff)
                        target.xV = velo * math.cos(angle)
                        target.yV = velo * math.sin(angle)
                    else:
                        target.xV = 0
                        target.yV = velo * (1 if yDiff > 0 else -1)
                    if xDiff < 0:
                        target.xV *= -1
                        target.yV *= -1
        # Now move the things
        movementDec(left.discs, right.discs, ball)
        if user:
            keys = pygame.key.get_pressed()
        for thing in discs:
            if thing.controlled:
                dirs = keys[pygame.K_LEFT] + keys[pygame.K_RIGHT] + keys[pygame.K_UP] + keys[pygame.K_DOWN]
                mul = 1/math.sqrt(2) if dirs == 2 else 1
                curAccel = accel * mul
                if keys[pygame.K_LEFT]:
                    thing.xV = max(thing.xV - curAccel, -thing.speed)
                if keys[pygame.K_RIGHT]:
                    thing.xV = min(thing.xV + curAccel, thing.speed)
                if keys[pygame.K_UP]:
                    thing.yV = max(thing.yV - curAccel, -thing.speed)
                if keys[pygame.K_DOWN]:
                    thing.yV = min(thing.yV + curAccel, thing.speed)
            else:
                comTarget = thing.target
                comTarget = (numpy.random.normal(comTarget[0], 6), numpy.random.normal(comTarget[1], 6))
                xToGo = comTarget[0] - thing.x
                yToGo = comTarget[1] - thing.y
                vectorMag = pythag(xToGo, yToGo)
                scale = abs(thing.speed/vectorMag)
                targetV = (xToGo*scale, yToGo*scale)
                if targetV[0] > thing.xV:
                    thing.xV = min(clamp(thing.xV + accel, -thing.speed, thing.speed), targetV[0])
                if targetV[0] < thing.xV:
                    thing.xV = max(clamp(thing.xV - accel, -thing.speed, thing.speed), targetV[0])
                if targetV[1] > thing.yV:
                    thing.yV = min(clamp(thing.yV + accel, -thing.speed, thing.speed), targetV[1])
                if targetV[1] < thing.yV:
                    thing.yV = max(clamp(thing.yV - accel, -thing.speed, thing.speed), targetV[1])

                """
                if thing.rad >= thing.x:
                    thing.x = thing.rad
                elif thing.x + thing.rad >= winX:
                    thing.x = winX-thing.rad
                if thing.rad >= thing.y:
                    thing.y = thing.rad
                elif thing.y + thing.rad >= winY:
                    thing.y = winY - thing.rad
                    """
        for thing in things:  # Move the stuff
            thing.x += thing.xV
            thing.y += thing.yV
            if thing.rad >= thing.x:  # Hit side wall left
                thing.xV = abs(thing.xV)
            elif thing.x + thing.rad >= winX:  # Hit side wall right
                thing.xV = -abs(thing.xV)
            if thing.rad >= thing.y:  # Hit ceiling
                thing.yV = abs(thing.yV)
            elif thing.y + thing.rad >= winY:  # Hit floor
                thing.yV = -abs(thing.yV)
            if thing.x < 0 or thing.x > winX or thing.y < 0 or thing.y > winY:  # Something is stuck
                barrierCrosses += 1
            if barrierCrosses > 100:
                reset(things)
                timeSinceKick = 0
                barrierCrosses = 0
            if isinstance(thing, Disc):  # Friction (only applies to discs)
                thing.xV *= 1 - decel
                thing.yV *= 1 - decel
        if ball.x <= ball.rad and goalTop <= ball.y <= goalBot:  # Goal
            if lastTouched in right.discs:
                lastTouched.goals += 1
            else:
                lastTouched.ownGoals += 1
            rightScore += 1
            reset(things, spot=-1)
            timeSinceKick = 0
        elif ball.x + ball.rad >= winX and goalTop <= ball.y <= goalBot:
            if lastTouched in left.discs:
                lastTouched.goals += 1
            else:
                lastTouched.ownGoals += 1
            leftScore += 1
            reset(things, spot=1)
            timeSinceKick = 0
        if user:
            out.fill(blackC)
            for thing in things:
                pygame.draw.circle(out, thing.color, [thing.x, thing.y], thing.rad)
                if thing.controlled:
                    text2 = font.render(f'YOU', True, whiteC)
                    textRect2 = text2.get_rect()
                    textRect2.center = (thing.x, thing.y)
                    out.blit(text2, textRect2)
                elif isinstance(thing, Disc):
                    font2 = pygame.font.Font('freesansbold.ttf', 12)
                    curText = font2.render(f'{thing.name}', True, whiteC)
                    curText2 = font2.render(f'{thing.speed} {thing.pow}', True, whiteC)
                    curTextRect = curText.get_rect()
                    curText2Rect = curText2.get_rect()
                    curTextRect.center = (thing.x, thing.y)
                    curText2Rect.center = (thing.x, thing.y+20)
                    out.blit(curText, curTextRect)
                    out.blit(curText2, curText2Rect)
                    pygame.draw.line(out, whiteC, (thing.x, thing.y), thing.target)
            out.blit(text, textRect)
            out.blit(textL, textRectL)
            out.blit(textR, textRectR)
            pygame.draw.line(out, whiteC, (0, goalTop), (25, goalTop))
            pygame.draw.line(out, whiteC, (0, goalBot), (25, goalBot))
            pygame.draw.line(out, whiteC, (winX - 25, goalTop), (winX, goalTop))
            pygame.draw.line(out, whiteC, (winX - 25, goalBot), (winX, goalBot))
            pygame.display.update()
    if user:
        pygame.quit()
    if leftScore > rightScore:
        winTeam = 'Blue wins!!!'
        left.wins += 1
        left.smallWins += 1
        right.smallLoss += 1
    elif rightScore > leftScore:
        winTeam = 'Orange wins!!!'
        right.wins += 1
        right.smallWins += 1
        left.smallLoss += 1
    else:
        winTeam = 'Game ended early.'
    # print(f'{left.ABR} {leftScore}-{rightScore} {right.ABR}')




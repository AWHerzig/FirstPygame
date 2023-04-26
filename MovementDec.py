from DirWide import *





def movementDec(left, right, ball):
    if rosterSize == 3:
        movement3(left, right, ball)
    elif rosterSize == 1:
        movement1(left, right, ball)


def movement1(left, right, ball):
    for disc in [left[0], right[0]]:
        pi = intercept(disc, ball)
        angle = math.atan((disc.y - pi[1]) / (disc.x - pi[0]))
        if -math.pi / 4 <= angle <= math.pi / 4 and isBehind(disc, ball):
            disc.target = pi
        else:
            disc.target = (50 if disc.side == -1 else winX - 50,
                           winY * .5 + (-60 if ball.y < winY * .35 else 60 if ball.y > winY * .65 else 0))


def movement3(left, right, ball):
    for team in [left.copy(), right.copy()]:
        if (ball.x <= winX / 2 and team[0].side == 1) or (ball.x >= winX / 2 and team[0].side == -1):  # Attacking
            toBall = closestBehind(team, ball)  # 1 goes to ball
            if toBall is not None:
                toBall.target = intercept(toBall, ball)
                toBall.name = 'O. TO BALL'
                team.remove(toBall)
            backup = farthestBack(team)  # 1 backs up the play
            if backup is not None:
                xSpot = winX * .35 if backup.side == -1 else winX * .65
                ySpot = winY * .4 if ball.y < winY * .33 else winY * .6 if ball.y > winY * .67 else winY * .5
                backup.target = (xSpot, ySpot)
                backup.name = 'O. Backup'
                team.remove(backup)
            xEdge = winX if team[0].side == -1 else 0
            yEdge = winY if ball.y >= winY * .5 else 0
            weakSide = closestTo(team, Spot(xEdge, yEdge))  # 1 plays weak side ball
            if weakSide is not None:
                xSpot = winX * .5
                ySpot = winY * .75 if ball.y < winY * .5 else winY * .25 if ball.y > winY * .5 else weakSide.startY
                weakSide.target = (xSpot, ySpot)
                weakSide.name = 'O. WEAKSIDE'
                team.remove(weakSide)
            for disc in team:  # Leftovers
                disc.name = 'O. LEFTOVER'
                xSpot = winX * .25 if team[0].side == -1 else winX * .75
                ySpot = winY * .5
                disc.target = (xSpot, ySpot)
        else:  # Defense
            toBall = closestBehind(team, ball)  # 1 goes to ball
            if toBall is not None:
                toBall.target = intercept(toBall, ball)
                toBall.name = 'D. TO BALL'
                team.remove(toBall)
            xSpot = winX*.17 if team[0].side == -1 else winX - winX*.17
            ySpot = winY * .5 + (-60 if ball.y < winY * .35 else 60 if ball.y > winY * .65 else 0)
            toGoal = closestTo(team, Spot(xSpot, ySpot))
            if toGoal is not None:  # 1 goes to goal
                toGoal.target = (xSpot, ySpot)
                toGoal.name = 'D. TO GOAL'
                team.remove(toGoal)
            xEdge = winX if team[0].side == -1 else 0

            yEdge = winY if ball.y >= winY * .5 else 0
            weakSide = closestTo(team, Spot(xEdge, yEdge))  # 1 plays weak side ball
            if weakSide is not None:  # 1 goes weakside
                xSpot = winX * .25 if weakSide.side == -1 else winX * .75
                ySpot = winY * .65 if ball.y < winY * .5 else winY * .35 if ball.y > winY * .5 else weakSide.startY
                weakSide.target = (xSpot, ySpot)
                weakSide.name = 'D. WEAKSIDE'
                team.remove(weakSide)
            for disc in team:  # Leftovers
                xSpot = winX * .1 if team[0].side == -1 else winX * .9
                ySpot = winY * .5
                disc.name = 'LEFTOVER'
                disc.target = (xSpot, ySpot)


def closestBehind(discs, ball):
    minDist = 10000000
    ind = -1
    for disc in discs:
        dist = distanceFormula(disc, ball)
        if dist < minDist and (
                (ball.x < disc.x and disc.side == 1) or (ball.x > disc.x and disc.side == -1) or min(winX - ball.x,
                                                                                                     ball.x) < winX * .1):
            minDist = dist
            ind = discs.index(disc)
    return discs[ind] if ind > -1 else None


def farthestBack(discs):
    fromGoal = winX
    ind = -1
    for disc in discs:
        dist = disc.x if disc.side == -1 else winX - disc.x
        if dist < fromGoal:
            fromGoal = dist
            ind = discs.index(disc)
    return discs[ind] if ind > -1 else None


def closestTo(discs, spot):
    minDist = 10000000
    ind = -1
    for disc in discs:
        dist = distanceFormula(disc, spot)
        if dist < minDist:
            minDist = dist
            ind = discs.index(disc)
    return discs[ind] if ind > -1 else None


def intercept(disc, ball):
    splitsFromNow = 0
    while splitsFromNow < 450:
        if ball.xV != 0:
            bruh = 4
        splitsFromNow += 10
        ballCurX = ball.x + (ball.xV * splitsFromNow)
        if ballCurX < 0:
            ballCurX *= -1
        elif ballCurX > winX:
            ballCurX -= 2 * (ballCurX - winX)
        ballCurY = ball.y + (ball.yV * splitsFromNow)
        if ballCurY < 0:
            ballCurY *= -1
        elif ballCurY > winY:
            ballCurY -= 2 * (ballCurY - winY)
        if disc.canCover(Spot(ballCurX, ballCurY, 5), splitsFromNow):
            # print('got there', round(distanceFormula(disc, ball)), splitsFromNow)
            return cornerCorrect(ballCurX, ballCurY)
    return cornerCorrect(ball.x, ball.y)


def cornerCorrect(x, y):
    if x < winX * .1 and y < winY * .1:
        return winX * .1, winY * .1
    if x > winX * .9 and y < winY * .1:
        return winX * .9, winY * .1
    if x < winX * .1 and y > winY * .9:
        return winX * .1, winY * .9
    if x > winX * .9 and y > winY * .9:
        return winX * .9, winY * .9
    return x, y


def isBehind(disc, ball):
    return (ball.x < disc.x and disc.side == 1) or (ball.x > disc.x and disc.side == -1)

# If in your own half, one goes to goal line, 1 goes to ball, one goes slightly off center weak side (40% depth?)
# In attacking half, 1 goes to ball, 1 goes to back up the play, 1 goes to weak side (50% depth?

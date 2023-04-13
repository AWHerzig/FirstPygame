from League import *
from Objects import *


#A.discs[2].controlled = True
#game(WAM, TUL, title='Check this shit out', watch=True)
def userplay():
    choice = int(input('1 to play, 2 to sim'))
    if choice == 1:
        for num in range(len(conferences)):
            print(f'Enter {num} for {getName(conferences[num][0], long)}')
        while True:
            try:
                conf = conferences[int(input('Which conference would you like to play in?'))]
                break
            except IndexError:
                pass
        for num in range(len(conf)):
            print(f'Enter {num} for {conf[num].name}')
        while True:
            try:
                userTeam = conf[int(input('Which conference would you like to play in?'))]
                break
            except IndexError:
                pass
        user = Disc(userTeam.ABR, 2, True)
        userStats = int(input('0 for Best Stats, 1 for Worst Stats, 2 for Average, 3 for Random'))
        options = [(9, 9), (3, 3), (6, 6), (user.speed, user.power)]
        user.speed = options[userStats][0]
        user.power = options[userStats][1]
        userTeam.discs[2] = user
        for i in userTeam.discs:
            print(i, i.speed, i.power)


userplay()
playIt()

from League import *
from Objects import *


#A.discs[2].controlled = True
#game(WAM, TUL, title='Check this shit out', watch=True)
def userplay():
    choice = int(input('1 to play, 2 to sim, 3 for 1v1'))
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
        userStats = int(input('0 for Best Stats, 1 for Worst Stats, 2 for Average, 3 for Random, 4 for god squad'))
        options = [(9, 9), (3, 3), (6, 6), (user.speed, user.pow), (9, 9)]
        user.speed = options[userStats][0]
        user.pow = options[userStats][1]
        userTeam.discs[0] = user
        if userStats == 4:
            for disc in userTeam.discs:
                disc.speed = 9
                disc.pow = 9
        userTeam.speed = 0
        userTeam.power = 0
        for i in userTeam.discs:
            print(i.speed, i.pow)
            userTeam.speed += i.speed
            userTeam.power += i.pow
        playIt()
    elif choice == 2:
        playIt()
    elif choice == 3:
        team1 = Team('Player 1', 'P1')
        team1.discs[0].speed = 9
        team1.discs[0].pow = 9
        team1.discs[0].controlled = 2
        team1.speed = 9
        team1.power = 9
        team2 = Team('Player 2', 'P2')
        team2.discs[0].speed = 9
        team2.discs[0].pow = 9
        team2.discs[0].controlled = True
        team2.speed = 9
        team2.power = 9
        game(team1, team2, 'P1 use WASD, P2 use arrows', True)


userplay()
#WAM.discs[0].controlled = True
#game(WAM, CHA, 'ooga booga', True)


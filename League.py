import pandas
import numpy
from Objects import *
from Gameplay import *
long = 'L'
short = 'S'  # I dunno why i need these but whatever


def series(team1, team2, l=3, title='', playoff=False, watch=False):
    #print(f'{team1} vs. {team2}')
    team1.wins = 0
    team2.wins = 0
    while team1.wins < l and team2.wins < l:
        game(team1, team2, title=title, watch=watch)
    if team1.wins == l:
        print(f'{team1} beats {team2} {team1.wins}-{team2.wins}!')
        if not playoff:
            team1.bigWins += 1
            team2.bigLoss += 1
        else:
            return team1
    else:
        print(f'{team2} beats {team1} {team2.wins}-{team1.wins}!')
        if not playoff:
            team2.bigWins += 1
            team1.bigLoss += 1
        else:
            return team2
# """


# TEAMS max 12 char (1 have 8, 4 have 10, 5 have 12)
CAAt = [Team('Charleston  ', 'CHA', purpleC, (128, 0, 0)), Team('Hofstra     ', 'HOF', (12, 46, 135), (255, 194, 17)),
        Team('UNCW        ', 'NCW', (0, 112, 115), (255, 215, 0)), Team('Northeastern', 'NE ', purpleC, (212, 27, 44)),
        Team('William&Mary', 'W&M', (17, 87, 64), (240, 179, 35)), Team('Monmouth    ', 'MON', (4, 30, 66), (83, 86, 90)),
        Team('Stony Brook ', 'SB ', (22, 36, 62), (153, 0, 0)), Team('Drexel      ', 'DRX', (0, 67, 123), (255, 218, 2)),
        Team('Deleware    ', 'DEL', (0, 83, 159), (255, 221, 49)), Team('Hampton     ', 'HAM', (0, 96, 169), orangeC),
        Team('Elon        ', 'ELN', purpleC, (115, 0, 10)), Team('Towson      ', 'TOW', purpleC, (255, 187, 0))]
WAM = CAAt[4]
CHA = CAAt[0]
# CAAt[4].discs[2].controlled = True

BEt =  [Team('Marquette   ', 'MAR', (0, 51, 102), (205, 204, 0)), Team('Xavier      ', 'XAV', (12, 35, 64), (158, 162, 163)),
        Team('Creighton   ', 'CRE', (0, 93, 170), (130, 130, 130)), Team('UConnecticut', 'CON', (0, 14, 47), (228, 0, 43)),
        Team('Providence  ', 'PRV', purpleC, (138, 141, 143)), Team('Seton Hall  ', 'SET', (0, 51, 160), (158, 162, 163)),
        Team('Villanova   ', 'VIL', (0, 32, 91), (139, 99, 75)), Team('Butler      ', 'BUT', (19, 41, 75), (116, 118, 120)),
        Team('DePaul      ', 'DeP', (0, 94, 184), (228, 0, 43)), Team('Georgetown  ', 'GEO', (4, 30, 66), (141, 129, 123))]

B12t = [Team('Kansas      ', 'KAN', (0, 81, 186), (232, 0, 13)), Team('Texas       ', 'TEX', purpleC, (191, 87, 0)),
        Team('Kansas State', 'KSU', (81, 40, 136), (167, 167, 167)), Team('Baylor      ', 'BAY', (21, 71, 52), (255, 184, 28)),
        Team('TCU         ', 'TCU', (77, 25, 121), (164, 189, 173)), Team('Iowa State  ', 'ISU', purpleC, (200, 16, 46)),
        Team('Oklahoma St ', 'OKs', purpleC, (255, 124, 25)), Team('Oklahoma    ', 'OK ', purpleC, (132, 23, 25)),
        Team('West VA     ', 'WVA', (0, 40, 85), (234, 170, 0)), Team('Texas Tech  ', 'TXT', purpleC, (204, 0, 0))]

ACCt = [Team('U Miami FL  ', 'MIA', (0, 80, 48), (244, 115, 33)), Team('Virginia    ', 'UVA', (35, 45, 75), (248, 76, 30)),
        Team('Duke        ', 'DUK', (0, 83, 155), orangeC), Team('Clemson     ', 'CLE', (82, 45, 128), (245, 102, 0)),
        Team('Pittsburgh  ', 'PIT', (0, 53, 148), (255, 184, 28)), Team('NC State    ', 'NCs', purpleC, (204, 0, 0)),
        Team('UNC         ', 'UNC', (123, 175, 212), orangeC), Team('Florida St  ', 'FLs', purpleC, (120, 47, 64)),
        Team('Syracuse    ', 'SYR', (0, 14, 84), (247, 105, 0)), Team('Notre Dame  ', 'ND ', (10, 134, 61), (201, 151, 0)),
        Team('Virginia T  ', 'VT ', purpleC, (99, 0, 49)), Team('Georgia Tech', 'GT ', (0, 48, 87), (179, 163, 105))]

B10t = [Team('Purdue      ', 'PUR', purpleC, (206, 184, 136)), Team('Indiana     ', 'IND', purpleC, (153, 0, 0)),
        Team('Northwestern', 'NW ', (78, 42, 132), orangeC), Team('Mich State  ', 'MIs', (24, 69, 59), orangeC),
        Team('Maryland    ', 'MD ', purpleC, (224, 58, 62)), Team('Illinois    ', 'ILL', (19, 41, 75), (232, 74, 39)),
        Team('Iowa        ', 'IOW', purpleC, (255, 205, 0)), Team('Michigan    ', 'MI ', (0, 39, 76), (255, 203, 5)),
        Team('Penn State  ', 'PAs', (4, 30, 66), orangeC), Team('Wisconsin   ', 'WIS', purpleC, (197, 5, 12)),
        Team('Ohio State  ', 'OHs', purpleC, (187, 0, 0)), Team('Nebraska    ', 'NEB', purpleC, (227, 25, 55))]

IVYt = [Team('Princeton   ', 'PRI', purpleC, (100, 31.8, 0)), Team('Yale        ', 'YAL', (0, 53, 107), orangeC),
        Team('Pennsylvania', 'PA ', (1, 31, 91), (153, 0, 0)), Team('Cornell     ', 'COR', (94, 57, 32), (166, 25, 46)),
        Team('Brown       ', 'BRO', (78, 54, 41), (228, 0, 43)), Team('Dartmouth   ', 'DAR', (0, 95, 47), orangeC),
        Team('Harvard     ', 'HAR', purpleC, (164, 16, 52)), Team('Columbia    ', 'COL', (155, 203, 235), orangeC)]

P12t = [Team('UCLA        ', 'UCL', (45, 104, 96), (242, 169, 0)), Team('Arizona     ', 'ARI', (0, 51, 102), (204, 0, 51)),
        Team('U South CA  ', 'USC', purpleC, (153, 27, 30)), Team('Oregon      ', 'ORE', (18, 71, 52), (254, 225, 35)),
        Team('Arizona St  ', 'ARs', purpleC, (140, 29, 64)), Team('Wash State  ', 'WAs', purpleC, (152, 30, 50)),
        Team('Colorado    ', 'CO ', purpleC, (207, 184, 124)), Team('Washington  ', 'WA ', (51, 0, 111), (232, 211, 162)),
        Team('Stanford    ', 'STA', purpleC, (140, 21, 21)), Team('California  ', 'CAL', (0, 50, 98), (253, 181, 21)),
        Team('Oregon State', 'ORs', purpleC, (220, 68, 5)), Team('Utah        ', 'UT ', purpleC, (204, 0, 0))]

SECt = [Team('Alabama     ', 'ALA', purpleC, (158, 27, 50)), Team('Kentucky    ', 'KEN', (0, 51, 160), orangeC),
        Team('Missouri    ', 'MO ', purpleC, (241, 184, 45)), Team('Tennessee   ', 'TEN', purpleC, (255, 130, 0)),
        Team('Vanderbilt  ', 'VAN', purpleC, (134, 109, 75)), Team('Georgia     ', 'UGA', purpleC, (186, 12, 47)),
        Team('S Carolina  ', 'SC ', purpleC, (115, 0, 10)), Team('Ole Miss    ', 'Ole', (22, 43, 72), (204, 9, 47)),
        Team('Louisiana SU', 'LSU', (70, 29, 124), (253, 208, 35)), Team('Arkansas    ', 'ARK', purpleC, (157, 34, 53)),
        Team('Florida     ', 'UFL', (0, 33, 165), (250, 70, 22)), Team('Auburn      ', 'AUB', (12, 35, 64), (232, 119, 34))]

A10t = [Team('Virginia CU ', 'VCU', purpleC, (255, 179, 0)), Team('Fordham     ', 'FOR', purpleC, (134, 0, 56)),
        Team('Duquesne    ', 'DUQ', (4, 30, 66), (186, 12, 47)), Team('George Mason', 'GM ', (30, 98, 56), (226, 168, 43)),
        Team('Davidson    ', 'DAV', purpleC, (172, 26, 47)), Team('Bonaventure ', 'StB', (84, 38, 26), (255, 199, 38)),
        Team('Rhode Island', 'RI ', (104, 171, 232), orangeC), Team('Loyola IL   ', 'LOY', (88, 41, 49), (253, 185, 19)),
        Team('UMass       ', 'MAS', purpleC, (151, 27, 47)), Team('Richmond    ', 'RIC', (0, 0, 102), (153, 0, 0))]

AACt = [Team('Houston     ', 'HOU', purpleC, (201, 42, 57)), Team('Memphis     ', 'MEM', (0, 48, 135), (137, 141, 141)),
        Team('Tulane      ', 'TUL', (0, 103, 71), (67, 176, 42)), Team('Cincinnati  ', 'CIN', purpleC, (224, 1, 34)),
        Team('Wichita St  ', 'WIC', purpleC, (255, 205, 0)), Team('E Carolina  ', 'EC ', (89, 42, 138), (253, 200, 47)),
        Team('S Florida   ', 'SFL', (0, 103, 71), (207, 196, 147)), Team('Temple      ', 'TEM', purpleC, (157, 34, 53)),
        Team('UC Florida  ', 'UCF', purpleC, (185, 155, 55)), Team('South MU    ', 'SMU', (53, 76, 161), (204, 0, 0))]

TUL = AACt[2]
CAAs = pandas.DataFrame(columns=['Team', 'Wins', 'Losses', 'GD'])
for i in CAAt:
    CAAs.loc[len(CAAs)] = [i, 0, 0, 0]
BEs = pandas.DataFrame(columns=['Team', 'Wins', 'Losses', 'GD'])
for i in BEt:
    BEs.loc[len(BEs)] = [i, 0, 0, 0]
B12s = pandas.DataFrame(columns=['Team', 'Wins', 'Losses', 'GD'])
for i in B12t:
    B12s.loc[len(B12s)] = [i, 0, 0, 0]
B10s = pandas.DataFrame(columns=['Team', 'Wins', 'Losses', 'GD'])
for i in B10t:
    B10s.loc[len(B10s)] = [i, 0, 0, 0]
ACCs = pandas.DataFrame(columns=['Team', 'Wins', 'Losses', 'GD'])
for i in ACCt:
    ACCs.loc[len(ACCs)] = [i, 0, 0, 0]
IVYs = pandas.DataFrame(columns=['Team', 'Wins', 'Losses', 'GD'])
for i in IVYt:
    IVYs.loc[len(IVYs)] = [i, 0, 0, 0]
P12s = pandas.DataFrame(columns=['Team', 'Wins', 'Losses', 'GD'])
for i in P12t:
    P12s.loc[len(P12s)] = [i, 0, 0, 0]
SECs = pandas.DataFrame(columns=['Team', 'Wins', 'Losses', 'GD'])
for i in SECt:
    SECs.loc[len(SECs)] = [i, 0, 0, 0]
A10s = pandas.DataFrame(columns=['Team', 'Wins', 'Losses', 'GD'])
for i in A10t:
    A10s.loc[len(A10s)] = [i, 0, 0, 0]
AACs = pandas.DataFrame(columns=['Team', 'Wins', 'Losses', 'GD'])
for i in AACt:
    AACs.loc[len(AACs)] = [i, 0, 0, 0]

conferences = [CAAt, BEt, B12t, B10t, ACCt, IVYt, P12t, SECt, A10t, AACt]
for conference in conferences:
    random.shuffle(conference)
random.shuffle(conferences)
cStandings = [CAAs, BEs, B12s, B10s, ACCs, IVYs, P12s, SECs, A10s, AACs]


def getName(team, length):
    if team in CAAt:
        return 'Colonial Athletic' if length in ['L', 'F', 'Long', 'Full'] else 'CAA'
    elif team in BEt:
        return 'Big East' if length in ['L', 'F', 'Long', 'Full'] else 'Big E'
    elif team in B12t:
        return 'Big 12' if length in ['L', 'F', 'Long', 'Full'] else 'Big 12'
    elif team in B10t:
        return 'Big 10' if length in ['L', 'F', 'Long', 'Full'] else 'Big 10'
    elif team in ACCt:
        return 'Atlantic Coastal' if length in ['L', 'F', 'Long', 'Full'] else 'ACC'
    elif team in IVYt:
        return 'Ivy League' if length in ['L', 'F', 'Long', 'Full'] else 'IVY'
    elif team in P12t:
        return 'Pac 12' if length in ['L', 'F', 'Long', 'Full'] else 'Pac 12'
    elif team in SECt:
        return 'Southeastern' if length in ['L', 'F', 'Long', 'Full'] else 'SEC'
    elif team in A10t:
        return 'Atlantic 10' if length in ['L', 'F', 'Long', 'Full'] else 'Atl 10'
    elif team in AACt:
        return 'American Athletic' if length in ['L', 'F', 'Long', 'Full'] else 'AAC'
    else:
        print('We got a problem')


class ConfPlayoff:
    def __init__(self, teams, name):
        self.QF = teams
        for i in range(6):
            self.QF[i].seed = i+1
        self.name = name
        self.SF = [teams[0], teams[1]]
        self.Final = []
        self.Winner = None
        self.stage = 'QF'

    def playNext(self):
        print(f'{self.name} {self.stage}')
        if self.stage == 'QF':
            self.SF.append(series(self.QF[2], self.QF[5], 3, f'{self.name} QF (bo{5})', playoff=True))
            self.SF.append(series(self.QF[3], self.QF[4], 3, f'{self.name} QF (bo{5})', playoff=True))
            self.stage = 'SF'
        elif self.stage == 'SF':
            self.Final.append(series(self.SF[0], self.SF[3], 3, f'{self.name} SF (bo{5})', playoff=True))
            self.Final.append(series(self.SF[1], self.SF[2], 3, f'{self.name} SF (bo{5})', playoff=True))
            self.stage = 'Final'
        elif self.stage == 'Final':
            self.Winner = series(self.Final[0], self.Final[1], 4, f'{self.name} Final (bo{7})', playoff=True)


class Regional:
    def __init__(self, teams, name):
        self.QF = teams
        for i in range(8):
            self.QF[i].seed = i+1
        self.name = name
        self.SF = []
        self.Final = []
        self.Winner = None
        self.stage = 'QF'

    def playNext(self):
        print(f'{self.name} {self.stage}')
        if self.stage == 'QF':
            self.SF.append(series(self.QF[0], self.QF[7], 3, f'{self.name} QF (bo{5})', playoff=True))
            self.SF.append(series(self.QF[1], self.QF[6], 3, f'{self.name} QF (bo{5})', playoff=True))
            self.SF.append(series(self.QF[2], self.QF[5], 3, f'{self.name} QF (bo{5})', playoff=True))
            self.SF.append(series(self.QF[3], self.QF[4], 3, f'{self.name} QF (bo{5})', playoff=True))
            self.stage = 'SF'
        elif self.stage == 'SF':
            self.Final.append(series(self.SF[0], self.SF[3], 3, f'{self.name} SF (bo{5})', playoff=True))
            self.Final.append(series(self.SF[1], self.SF[2], 3, f'{self.name} SF (bo{5})', playoff=True))
            self.stage = 'Final'
        elif self.stage == 'Final':
            self.Winner = series(self.Final[0], self.Final[1], 4, f'{self.name} Final (bo{7})', playoff=True)


def standingsUpdate():
    for con in cStandings:
        con.Wins = [team.bigWins for team in con.Team]
        con.Losses = [team.bigLoss for team in con.Team]
        con.GD = [team.smallWins - team.smallLoss for team in con.Team]
        con.sort_values(['Wins', 'GD'], inplace=True, ascending=False, ignore_index=True)
    for con in cStandings:
        print(f'{getName(con.iloc[0, 0], long)} standings')
        print(con)


def roundRobin(groups):
    for q in range(1):  # This is a slightly edited of a round robin algorithm i found online and stole
        schedule = [[]]*11
        for div in groups:
            w = div.copy()
            random.shuffle(w)
            if len(w) % 2 == 1:
                w.append(None)
            n = len(w)
            d = list(range(n))
            mid = n // 2
            for i in range(n - 1):
                l1 = d[:mid]
                l2 = d[mid:]
                l2.reverse()
                round = []
                for j in range(mid):
                    t1 = w[l1[j]]
                    t2 = w[l2[j]]
                    if j == 0 and i % 2 == 1:
                        round.append((t2, t1))
                    else:
                        round.append((t1, t2))
                schedule[i] = schedule[i] + round
                # rotate list by n/2, leaving last element at the end
                d = d[mid:-1] + d[:mid] + d[-1:]
        return schedule  # returns [[()]]


def playIt():
    schedule = roundRobin(conferences)
    autoQual = []
    playIn = []
    for roundNum in range(len(schedule)):
        print('ROUND', roundNum + 1)
        for matchup in schedule[roundNum]:
            series(matchup[0], matchup[1], 2, f'{getName(matchup[0], short)} reg season (bo{3})')
            # pass
        standingsUpdate()
    if seasonLength > 1:
        for roundNum in range(len(schedule)):
            print('ROUND', roundNum + 12)
            for matchup in schedule[roundNum]:
                series(matchup[1], matchup[0], 2, f'{getName(matchup[0], short)} reg season (bo{3})')
            standingsUpdate()
    cPlayoffs = [ConfPlayoff(con.iloc[0:6, 0], getName(con.iloc[0, 0], short)) for con in cStandings]
    for i in range(3):
        for con in cPlayoffs:
            con.playNext()
            if i == 2:
                con.Winner.confWinner = 1
                autoQual = autoQual + con.Final
                for team in con.SF:
                    if team not in autoQual:
                        playIn.append(team)
    tournament(autoQual, playIn)


def tournament(qualified, playin):
    playinDF = pandas.DataFrame(columns=['Team', 'Wins', 'Losses', 'GD'])
    for i in playin:
        i.seed = 0
        playinDF.loc[len(playinDF)] = [i, i.bigWins, i.bigLoss, i.smallWins-i.smallLoss]
    playinDF.sort_values(['Wins', 'GD'], inplace=True, ascending=False, ignore_index=True)
    print('Play-In seeding')
    print(playinDF)
    pTeams = list(playinDF.Team)
    qualified = qualified + pTeams[0:4]
    for seed in range(4, 12):
        qualified.append(series(pTeams[seed], pTeams[23-seed], 3, f'PLAY-IN (bo{5})', playoff=True))
    tourneyDF = pandas.DataFrame(columns=['Team', 'Wins', 'Losses', 'GD', 'Con Win'])
    for i in qualified:
        i.seed = 0
        tourneyDF.loc[len(tourneyDF)] = [i, i.bigWins, i.bigLoss, i.smallWins - i.smallLoss, i.confWinner]
    print('Tournament Seeds (conference winners get top seeds')
    tourneyDF.sort_values(['Con Win', 'Wins', 'GD'], inplace=True, ascending=False, ignore_index=True)
    print(tourneyDF)
    teamsSorted = numpy.array(list(tourneyDF.Team))
    regions = [Regional(teamsSorted[[0, 7, 8, 15, 16, 23, 24, 31]], 'NE Regional'),
               Regional(teamsSorted[[1, 6, 9, 14, 17, 22, 25, 30]], 'NW Regional'),
               Regional(teamsSorted[[2, 5, 10, 13, 18, 21, 26, 29]], 'SE Regional'),
               Regional(teamsSorted[[3, 4, 11, 12, 19, 20, 27, 28]], 'SW Regional')]
    finalFour = []
    for roundNum in range(3):
        for region in regions:
            region.playNext()
            if roundNum == 2:
                finalFour.append(region.Winner)
    print('WELCOME TO THE FINAL FOUR')
    Final1 = series(finalFour[0], finalFour[3], 4, 'FINAL FOUR (bo7)', playoff=True)
    Final2 = series(finalFour[1], finalFour[2], 4, 'FINAL FOUR (bo7)', playoff=True)
    print('NATIONAL CHAMPIONSHIP')
    winner = series(Final1, Final2, 4, 'NATIONAL CHAMPIONSHIP (bo7)', playoff=True)
    print(winner, 'are the national champions!!')

#"""

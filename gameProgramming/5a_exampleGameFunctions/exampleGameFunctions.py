# Example Game Functions Project, Nevaeh Copeland, v0.4
import random

# add List to pick opposing Teams

randomOpposingTeams = 'Kansas Jayhawks, Purdue Boilermakers, Arizona Wilcats, Marquette Golden Eagles, UConn Huskies, Houston Cougars, Tennessee Volunteers, Creighton Bluejays, Duke Devils, Florida Atlantic Owls, Gonzaga Bulldogs, Miami Hurricanes, Arkansas Razorbacks, Baylor Bears, South Carolina Trojans, Kentucky Wildcats, Michigan State Spartans, Texas Longhorns, North Carolina Tar Heels, Villanova Wildcats, Alabama Crimson Tide, Illinois Fighting Illini, James Madision Dukes, Colorado Buffaloes'.split(',')

# Add jumpball function
# Add shooting function
# Add point counter function
# Add random team for opponent function






def getRandomTeam(randomOpposingTeams):
    opposingTeam = random.randint(0, len(randomOpposingTeams) - 1 )
    print(f'Your oppnents today are the{randomOpposingTeams[opposingTeam]}')
    return randomOpposingTeams[opposingTeam]

team = getRandomTeam(randomOpposingTeams)

def jumpBall(skillLevel, centerHeight, team):
    if centerHeight >= 72 or skillLevel >= 3.5:
        print(f'The{team} have the ball')
    else: # This block happens when blah blah blah.   
        print('Your Team has the ball')

jumpBall(3, 75, team)

def shootBall(playerHeight, opponentSkill, playerSkill):
    if playerHeight >= 3 and opponentSkill >= 3:
        print('They fouled you. You get two freethrows!')
        if playerSkill >= 3.5:
            print('You scored both points!')
        if playerSkill <= 3:
            print('You missed both..keep your head up!')
        else:
            print('You missed one!')


def countPoints():
    if
    pass

# Introduce the game
# print('Welcome to your Freshman year as a college asketball player.\n This game was created by Nevaeh Copeland')



# def functionOne():
#     pass
# def functionTwo(param1):
#     pass
# def functionThree(param1 = "Default Value"):
#     pass
# def function(Param1, param2, param3):
#     pass
# def catchBall(throwQuality, passCatchScore, weather):
#     if throwQuality > 5.0 and passCatchScore >= 90 and weather == 'Sunny':
#         ballCaught = True
#     elif throwQuality > 4.0 and passCatchScore >= 75 and weather == 'Windy':
#         ballCaught = False
#     else:
#         print("Oh, no...INTERCEPTION!/n")
#         ballIntercepted = True
#         return ballIntercepted
#     return ballCaught
# catchBall(4.25, 107, 'Rainy')

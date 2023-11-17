# Example Game Functions Project, Nevaeh Copeland, v0.6
import random

# add List to pick opposing Teams

randomOpposingTeams = 'Kansas Jayhawks,Purdue Boilermakers,Arizona Wilcats,Marquette Golden Eagles,UConn Huskies,Houston Cougars,Tennessee Volunteers,Creighton Bluejays,Duke Devils,Florida Atlantic Owls,Gonzaga Bulldogs,Miami Hurricanes,Arkansas Razorbacks,Baylor Bears,South Carolina Trojans,Kentucky Wildcats,Michigan State Spartans,Texas Longhorns,North Carolina Tar Heels,Villanova Wildcats,Alabama Crimson Tide,Illinois Fighting Illini,James Madision Dukes,Colorado Buffaloes'.split(',')
finalScore = 0
opponentFinalScore = 0
# Add jumpball function
# Add shooting function
# Add point counter function
# Add random team for opponent function


skillLevelOptions = list(range(1,101))
centerHeightOptions = list(range(1,101))

playerHeightOptions = list(range(1,101))
playerSkillOptions = list(range(1,101))

opponentHeightOptions = list(range(1,101))
opponentSkillOptions = list(range(1,101))


# skillLevel = random.randrange((0,2)-1)
# centerHeight = random.randint(0,100)

def getRandomTeam(randomOpposingTeams):
    opposingTeam = random.randint(0, len(randomOpposingTeams) - 1 )
    print(f'\nYour opponents today are the {randomOpposingTeams[opposingTeam]}.')
    print('Prepare for jump ball.\n')
    return randomOpposingTeams[opposingTeam]

team = getRandomTeam(randomOpposingTeams)

def jumpBall(skillLevel, centerHeight, team):
    if centerHeight >= 72 or skillLevel >= 3.5:
        print(f'The {team} have the ball')
    else: # This block happens when blah blah blah.   
        print('Your Team has the ball')

skillLevel = random.randint(0, len(skillLevelOptions))
centerHeight = random.randint(0,len(centerHeightOptions))

jumpBall(skillLevel, centerHeight, team)
# freethrow function

def freeThrow(playerSkill):
    if playerSkill > 3:
        print('You scored both points!')
        finalScore = +2

    if playerSkill == 3:
       print('You missed one. Half Decent!')
       opponentFinalScore = +2
    if playerSkill < 3:
        print('You missed both and the other team scored with the rebound. \n Keep your head up!')

playerHeight = random.randint(0,len(playerHeightOptions))
playerSkill = random.randint(0,len(playerSkillOptions))

opponentHeight = random.randint(0,len(opponentHeightOptions))
opponentSkill = random.randint(0,len(opponentSkillOptions))

def shootBall(playerHeight, playerSkill, opponentHeight, opponentSkill):
    print('Your team is on offense and your teammate has passed you the ball.')
    if playerHeight > opponentHeight:
        print('They fouled you. You get two freethrows!')
        freeThrow(playerSkill)
    elif playerSkill > opponentSkill :
        print('You hit a three-point shot right in their face!')
        finalScore = +2
    elif playerSkill < opponentSkill:
        print('They stole the ball and dunked. Lock in next time!')
        opponentFinalScore = +2
    else:
        print('Both of you have a similar skill set. The ref has called jump ball.')
        jumpBall()

shootBall (playerHeight, playerSkill, opponentHeight, opponentSkill)
playerHeight = random.randint(0,len(playerHeightOptions))
playerSkill = random.randint(0,len(playerSkillOptions))
opponentHeight = random.randint(0,len(opponentHeightOptions))
opponentSkill = random.randint(0,len(opponentSkillOptions))

shootBall (playerHeight, playerSkill, opponentHeight, opponentSkill)
playerHeight = random.randint(0,len(playerHeightOptions))
playerSkill = random.randint(0,len(playerSkillOptions))
opponentHeight = random.randint(0,len(opponentHeightOptions))
opponentSkill = random.randint(0,len(opponentSkillOptions))



# def countPoints():
#     print('The Final Score was {finalScore}')
#     if finalScore > opponentFinalScore:



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

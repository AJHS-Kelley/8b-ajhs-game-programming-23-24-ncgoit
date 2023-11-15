# Example Game Functions Project, Nevaeh Copeland, v0.3
import random

# add List to pick opposing Teams

randomOpposingTeams = ['Kansas Jayhawks, Purdue Boilermakers, Arizona Wildcats, Marquette Golden Eagles, UConn Huskies, Houston Cougars, Tennessee Volunteers, Creighton Bluejays, Duke Devils, Florida Atlantic Owls, Gonzaga Bulldogs, Miami Hurricanes, Arkansas Razorbacks, Baylor Bears, South Carolina Trojans, Kentucky Wildcats, Michigan State Spartans, Texas Longhorns, North Carolina Tar Heels, Villanova Wildcats, Alabama Crimson Tide, Illinois Fighting Illini, James Madision Dukes, Colorado Buffaloes' .split()]

# Add jumpball function
# Add shooting function
# Add point counter function
# Add random team for opponent function

wordIndex = random.randint(0, len(randomOpposingTeams) - 1)




def getRandomTeam(randomOpposingTeams):
    opposingTeam = random.randint(0,len(randomOpposingTeams) - 1 )
    return randomOpposingTeams[opposingTeam]
    pass

def getRandomTeam():
    pass


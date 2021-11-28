import math
import os
from pathlib import Path
from ExperimentalData import ExperimentalData
import json

#gunname = "AK-74M"
#calibre = "5.45"
#munition = "5.45 x 39"
#velocity = 900
#weight = 3.43
#buildname = "Caribbean Sea View"
#buildheight = 102
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

def CalcSpeed(experimentalData: ExperimentalData):
    planet = planets.index(experimentalData.planet)
    time = math.sqrt((2*experimentalData.buildheight)/(g_ms2[planet]))
    distance = (experimentalData.velocity * time)
    print("When a projectile is fired with a " + experimentalData.gunname + " of calibre " + experimentalData.calibre +  " with ammunition of " + experimentalData.munition + " off of the building with name " + experimentalData.buildname + " with height " + str(experimentalData.buildheight) + " meters at a velocity of " + str(experimentalData.velocity) + " m/s on the planet " + experimentalData.planet + ", the bullet ends up taking " + str(float(time)) + " seconds and travels a total of " + str(float(distance)) + " meters")

#experimentalData = ExperimentalData("AK-74M", "5.45", "5,45 x 39", 900, 3.43, "Caribbean Sea View", 102, "Saturn") 
#(experimentalData)

mydataset = [
ExperimentalData("AK-74M", "5.45", "5.45 x 39mm", 900, 3.43, "Burj Khalifa", 828, "Earth"),
ExperimentalData("AK-74M", "5.45", "5.45 x 39mm", 900, 3.43, "Merdeka 118", 644, "Jupiter"),
ExperimentalData("AK-74M", "5.45", "5.45 x 39mm", 900, 3.43, "Shanghai Tower", 632, "Uranus"),
ExperimentalData("AK-74M", "5.45", "5.45 x 39mm", 900, 3.43, "Abraj Al-Bait Clock Tower", 601, "Mercury")
]

for data in mydataset:
    print("\n---------------------------------------------------------------------\n")
    CalcSpeed(data)

#serialization

myoutputpath = Path(__file__).parents[0]
myoutputfilepath = os.path.join(myoutputpath, 'Projectile-Motion.json')

print(myoutputfilepath)

with open(myoutputfilepath, 'w') as outfile:
    json.dump([data.__dict__ for data in mydataset], outfile)

#def CalcSpeed(gunnames,calibres,ammunition,velocity2, height):
    #time = math.sqrt((2*height)/9.8)
    #distance = (velocity2 * time)
    #print("When a projectile is fired with a " + gunnames + " of calibre " + calibres +  "with ammunition of " + munition + " off of the building with height " + str(height) + " meters at a velocity of " + str(velocity2) + " m/s, the bullet ends up taking " + str(float(time)) + " seconds and travels a total of " + str(float(distance)) + " meters")

#CalcSpeed(gunname, calibre, munition, velocity, buildheight)
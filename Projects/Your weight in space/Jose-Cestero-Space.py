planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

print("This program calculates your weight on the solar system depending on the planet")
weight = int(input("What is your weight in pounds? "))

Planet = input("Select a planet from the list here: "+ str(planets))

def CalcWeight(planets, weights):
    kg = weights/2.2046

    print("Your mass in kg is "+ str(kg))

    nlb = 4.45
    planet = str(planets)
    planet_index = planets.index(planets)
    print("Your weight in " + Planet + " is " + str((kg * (g_ms2[planet_index]))/nlb) + " lb")

CalcWeight(Planet, weight)

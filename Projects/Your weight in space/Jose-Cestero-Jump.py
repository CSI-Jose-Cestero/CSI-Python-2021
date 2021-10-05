planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
rel_grv = [2.65, 1.11, 1, 2.64, 0.40, 0.94, 1.13, 0.88]

print("Jump Calculator!!!")
print("This program calculates how long you would jump on different planets")
lengths = float(input("How long is your jump on Earth in meters? "))

Planet = input("Select a planet from the list here: "+ str(planets))
def CalcJumps(planet, ln):
    print("The length of your jump on earth is " + str(ln) + "m")
    planet_index = planets.index(planet)
    print("The length of your jump in " + Planet + " is " + str(ln*rel_grv[planet_index]) + "m")

CalcJumps(Planet, lengths)
# print("Hello World!")
# print("What is your name?")
# myName= input()
# print("It's good to see you" + myName)
# print("The length of your name is: " + len(myName))
# print("What is your age?")
# myAge = input()
# print("Your age is: " + myAge)

print("   / \ ")
print("  /   \ ")
print(" /_____\ ")
print("This program finds the area of a triangle")

print("What is the base of the triangle?")
base = int(input())
print("What is the height of the triangle?")
height = int(input())
print("The base of the triangle is " + str(base) + " and the height of the triangle is " + str(height))
area = 1/2 * base * height
print("The area of the triangle is " + str(area))

def PrintAreaTriangle(base, height):
  area = base*height*1/2
  print("The base is " + str(base) + ", the height is " + str(height) + ", and the area of the triangle is " + str(area))


PrintAreaTriangle(base, height)
PrintAreaTriangle(123, 4)

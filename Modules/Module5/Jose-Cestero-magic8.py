import random

name = input("What's your name? ")
print("Hello "+ name + "! You're using a Magic 8 Ball!")

question = input("So, what do you want to ask me? ")
print(name +" asks: "+question)

rannum = random.randint(1, 12)
if (rannum == 1):
    print("Yes - definitely.")
elif (rannum == 2):
    print("It is decidedly so.")
elif (rannum == 3):
    print("Without a doubt.")
elif (rannum == 4):
    print("Reply hazy, try again.")
elif (rannum == 5):
    print("Ask again later.")
elif (rannum == 6):
    print("Better not tell you now.")
elif (rannum == 7):
    print("My sources say NO.")
elif (rannum == 8):
    print("Outlook not so good.")
elif (rannum == 9):
    print("Very doubtful.")
elif (rannum == 10):
    print("Don't expect it.")
elif (rannum == 11):
    print("I can bet on it being true.")
elif (rannum == 12):
    print("The outcome is uncertain.")


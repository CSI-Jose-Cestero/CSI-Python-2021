import random


print("Rock, paper, scissors!!!!!")
options = ["rock", "paper", "scissors"]
choices = input("Choose between rock, paper, and scissors! ")

def input(pick):
    number = random.randint(0, 2)
    compchoice = options[number]
    print("The computer chose " +compchoice + " and you chose " + pick)
    if(compchoice == pick):
        print("Because you both chose the same option, it's a tie!")
    elif(compchoice== "scissors" & pick == "rock"):
        print("Rock beats scissors, you win!")
    elif(compchoice== "scissors" & pick == "paper"):
        print("Scissors beats paper, you lose.")
    elif(compchoice== "paper" & pick == "scissors"):
        print("Scissors beats paper, you win!")
    elif(compchoice== "paper" & pick == "rock"):
        print("Paper beats rock, you lose.")
    elif(compchoice== "rock" & pick == "paper"):
        print("Paper beats rock, you win!")
    elif(compchoice== "rock" & pick == "scissors"):
        print("Rock beats scissors, you lose.")

input(choices)

    

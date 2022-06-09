
from ast import Pass
import random
from sre_constants import IN

def player_input():
    player_choice = input("Select an option: Rock, Paper or Scissors \n")

    if player_choice in ["Rock", "rock", "r", "R", "ROCK"]:
        player_choice = "R"

    elif player_choice in ["Paper", "paper", "p", "P", "PAPER"]:
        player_choice = "P"

    elif player_choice in ["Scissors", "scissors", "s", "S", "SCISSORS"]:
        player_choice = "S"

    else:
        print("Invalid Input, Try Again")
        player_input()

    return player_choice


def computer_input():
    cpu_choice = random.randint(1,3)
    if cpu_choice == 1:
        cpu_choice = "R"
    elif cpu_choice == 2:
        cpu_choice = "P"
    else:
        cpu_choice = "S"
    
    print (f"\n YOU({player_choice}): CPU({cpu_choice})\n")

    return cpu_choice


while True:
    print("")
    player_choice = player_input()
    cpu_choice = computer_input()
    print("")

    if player_choice == "R":
        if cpu_choice == "R":
            print("It is a tie")
        elif cpu_choice == "P":
            print("Paper > Rock! CPU wins")
        elif cpu_choice == "S":
            print("Rock > Scissors! You win")

    elif player_choice == "P":
        if cpu_choice == "R":
            print("Paper > Rock! You win")
        elif cpu_choice == "P":
            print("It is a tie")
        elif cpu_choice == "S":
            print("Scissors > Paper! CPU wins")

    elif player_choice == "S":
        if cpu_choice == "P":
            print("Scissors > Paper! You win")
        elif cpu_choice == "S":
            print("It is a tie")
        elif cpu_choice == "R":
            print("Rock > Scissors! CPU wins")


    player_choice = input("Do you want to play again? (y/n) \n")
    if player_choice in ["Y", "y", "yes", "Yes", "YES"]:
        Pass
    elif player_choice in ["N", "n", "No", "NO", "no"]:
        break
    else:
        break
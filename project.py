import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock ,paper, or scissors? : ").lower()

    if player == computer:
        print("computer :", computer)
        print("player :",player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer :", computer)
            print("player :", player)
            print("You LOSE")
        if computer == "scissors":
            print("computer :", computer)
            print("player :", player)
            print("You WIN!")

    elif player == "scissors":
        if computer == "paper":
            print("computer :", computer)
            print("player :", player)
            print("You WIN!")
        if computer == "rock":
            print("computer :", computer)
            print("player :", player)
            print("You Lose!")

    elif player == "paper":
        if computer == "rock":
            print("computer :", computer)
            print("player :", player)
            print("You WIN!")
        if computer == "scissors":
            print("computer :", computer)
            print("player :", player)
            print("You LOSE!")

    play_again = input("play again? (yes/no) :").lower()

    if play_again != "yes":
        break
print("BYEEEEEE")
# rps_game.py
import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Enter rock, paper, scissors or 'exit': ").lower()
    
    if user == "exit":
        break
    
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    
    if user == computer:
        print("It's a Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
    else:
        print("You Lose!")
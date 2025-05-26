"""
author: Ashya
filename: RockPaperScissorsGame.py
objective: Create a game where the player can play against the computer by choosing rock, 
 paper or scissors, and the computer randomly selects a choice
"""
# going to attempt code annotation storytelling as a study technique
import random
#randomizes the computer's actions, importing a random module

""" taking user input and making computer choose """
user_action = input("Please enter your choice: (rock, paper, scissors)")
user_actions = ["rock", "paper", "scissors"]
#defined list of options 
computer_action = random.choice(user_actions)
#computer randomly selects between the actions listed

print(f"\nYour move {user_action}, Computer's move {computer_action}.\n") 
#prints the actions of the user and computer

""" determining the winner """
if user_action == computer_action:
    print("It's a tie!")
elif user_action == "rock" and computer_action == "scissors":
    print("You win!") 
elif user_action == "paper" and computer_action == "rock":
    print("You win!")
elif user_action == "scissors" and computer_action == "paper":
    print("You win!")
else: 
    print("Computer wins!")
#if elif else block

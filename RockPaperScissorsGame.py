"""
author: Ashya
filename: RockPaperScissorsGame.py
objective: Create a game where the player can play against the computer by choosing rock, 
 paper or scissors, and the computer randomly selects a choice
"""
import random
#randomizes the computer's actions

""" taking user input and making computer choose """
user_action = input("Please enter your choice: (rock, paper, scissors)")
user_actions = ["rock", "paper", "scissors"]
computer_actions = random.choice(user_actions)
# computer randomly selects between the actions listed

print(f"\nYour move {user_action}, computer's move {computer_action}.\n") 
#prints the actions of the user and computer

""" determining the winner """
if user_action == computer_action:
    print("You both made the same move {user_action}. It's a tie!")
elif user_action == "rock":
    if computer+action == "scissors":
#if elif else block

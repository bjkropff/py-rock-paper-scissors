#!/usr/bin/env python3.7.6
import random

print("Get ready to play Rock-Paper-Scissors")

total_bill=input("What is the total of the bill?: ")

#Computer choice
comp = random.randint(0, 2)

#Paper -> Rock -> Scissors
#Scissors -> Paper -> Rock
#Rock -> Scissors -> Paper

rock_check = ["Paper", "Rock", "Scissors"]
paper_check = [ "Scissors", "Paper", "Rock"]
scissors_check = ["Rock", "Scissors", "Paper"]

#outcomes[0] compares rock to player input
#outcomes[1] compares paper to player input
#outcomes[2] compares scissors to player input
outcomes = [rock_check, paper_check, scissors_check]


def player_choice():
#Player choice
  print("Please choose one:")
  print("1. Rock")
  print("2. Paper")
  print("3. Scissors")
  player_pick = input("Choice: 1, 2, 3")

  return player_pick

player_pick = player_choice()

if player_pick not in [1, 2, 3]:
	print("Looks like that is not a valid choice".)
	print("1. Rock")
  print("2. Paper")
  print("3. Scissors")
  player_pick = input("Please pick: 1, 2, or 3:")
  else
    player_choice()
#Valid input check
  

player_choice()

compare_list = outcomes[player]

#Compare choice and outcome

#if player is higher than comp
#Example 1 != 2
if player > comp 

play wins

if comp > play

comp wins

#Example 1 = 1
else tie
#Outcome

comp = 1,2,3
play = 0,1,2

# Scissors -> Paper
# Paper -> Rock
# Rock -> Scissors


# Paper -> Rock -> Scissors
# Scissors -> Paper -> Rock
# Rock -> Scissors -> Paper


def winner_check(comp):
    match comp:
        case "Scissors":
            return "Bad request"
        case "Paper":
            return "Not found"
        case "Rock":
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"



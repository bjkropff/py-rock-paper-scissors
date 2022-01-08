#!/usr/bin/env python3
import random

print("Get ready to play Rock-Paper-Scissors")

#Idea for how to resolve the comparison
#Paper -> Rock -> Scissors
#Scissors -> Paper -> Rock
#Rock -> Scissors -> Paper

rock_check = ["Paper", "Rock", "Scissors"]
paper_check = [ "Scissors", "Paper", "Rock"]
scissors_check = ["Rock", "Scissors", "Paper"]

outcomes = [rock_check, paper_check, scissors_check]

#Computer choice and list picking
comp = random.randint(0, 2)
compare_list = outcomes[comp]

#Take player choice and verify it is an accepted option
def player_choice():
  print("Please choose one: Rock; Paper; Scissors")
  pick = input("Pick: ")
  
  #Valid input check 
  while pick not in compare_list:
    print("Looks like that is not a valid choice.")
    pick = player_choice()

  return pick

#Gather player and comp picks; comp with always be at index 1
player_pick = player_choice()
comp_pick = compare_list[1]

#Function for repeat printing
def gamedetails (player_pick, comp_pick):
		print("You pick " + player_pick)
		print("The computer picked " + comp_pick)

#Game logic
if compare_list.index(player_pick) == 2 :
		gamedetails (player_pick, comp_pick)
		print("Computer wins")
elif compare_list.index(player_pick) == 0  :
		gamedetails (player_pick, comp_pick)
		print("You win")
elif compare_list.index(player_pick) == 1  :
		gamedetails (player_pick, comp_pick)
		print("It's a tie")
else : 
		print("Something happened; try again")

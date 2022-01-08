#!/usr/bin/env python3
import random

print("Get ready to play Rock-Paper-Scissors")

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

compare_list = outcomes[comp]

#Player choice
def player_choice():
  print("Please choose one: Rock; Paper; Scissors")
  pick = input("Pick: ")
  
  #Valid input check 
  while pick not in compare_list:
    print("Looks like that is not a valid choice.")
    pick = player_choice()

  return pick

player_pick = player_choice()
comp_pick = compare_list[1]

#compare_list is the list of outcomes: index 0 beats comp, index 1 is a tie,  index 2 loes 
#player_pick is the player choice 

#Find index of player choice
# if index 0 player wins
# if index 1 tie
# if index 2 comp wins
def gamedetails (player_pick, comp_pick):
		print("You pick " + player_pick)
		print("The computer picked " + comp_pick)

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




# index = animals.index('dog')


# if compare_list.index(comp) == 


# #Compare choice and outcome

# #if player is higher than comp
# #Example 1 != 2
# if player > comp 

# play wins

# if comp > play

# comp wins

# #Example 1 = 1
# else tie
# #Outcome

# comp = 1,2,3
# play = 0,1,2

# # Scissors -> Paper
# # Paper -> Rock
# # Rock -> Scissors


# # Paper -> Rock -> Scissors
# # Scissors -> Paper -> Rock
# # Rock -> Scissors -> Paper
# index = animals.index('dog')





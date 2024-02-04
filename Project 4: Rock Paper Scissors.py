

# This code will let you play rock paper scissors with the computor



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random


def play_game():
  #user
  user = int(input("\nInstructions: \nFor rock enter 0, for paper enter 1 and for scissors enter 2.\nenter your choice: \n"))
  if user == 0:
    print("user \n" + rock)
  elif user == 1:
    print("user \n" + paper)
  elif user == 2:
    print("user \n" + scissors)
  else:
    print("invalid input")


  #coumputer
  ran_game = random.randint(0,2)
  if ran_game == 0:
    print("computer \n" + rock)
  elif ran_game == 1:
    print("computor \n" + paper)
  else:
    print("computor \n" + scissors)


  if ran_game == 0 and user == 1:
    print("you win")
  elif ran_game == 1 and user == 2:
    print("you win")
  elif ran_game == 2 and user == 0:
    print("you win")
  elif ran_game == user:
    print("draw")
  else:
    print("you lose")

play_game_ = True 
while play_game_:
  play_game()
  user_input = input("Play Again? \n")
  if user_input == "no":
    play_game_ = False
    



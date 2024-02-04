import random

logo = ''''     ___                       _   _                                   _               
'    / _ \_   _  ___  ___ ___  | |_| |__   ___    _ __  _   _ _ __ ___ | |__   ___ _ __ 
'   / /_\/ | | |/ _ \/ __/ __| | __| '_ \ / _ \  | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
'  / /_\\ | |_| |  __/\__ \__ \ | |_| | | |  __/  | | | | |_| | | | | | | |_) |  __/ |   
'  \____/ \__,_|\___||___/___/  \__|_| |_|\___|  |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
'                                                                                       
'''

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
  lives = 10
elif difficulty == 'hard':
  lives = 5
print(f"You have {lives} attempts remaining to guess the number.")
random_number = random.randint(1,100)
end_game = False
while end_game == False:
  user_number = int(input("make a guess: "))
  if lives == 0:
    print("You are out of lives\n*******GAME OVER*****")
    break
  elif user_number == random_number:
    end_game = True
    print(f"You got it! The answer was {random_number}.")
  elif user_number > random_number:
    print("Too high.\nGuess again.")
  elif user_number < random_number:
    print("Too low.\nGuess again.")
  lives -= 1
  print(f"you have {lives} left")
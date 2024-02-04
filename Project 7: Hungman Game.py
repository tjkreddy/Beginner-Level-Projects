#Step 1 


#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''',''' ''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
length = len(chosen_word)
list = []
for char in range (0,int(length)):
  list.append("_")
print(list)
i=0
lives = 7
end_game = False
while end_game == False:
  user_guess = input("\n\nEnter the guess letter:\n")
  user_guess = user_guess.lower()
  count = 0
  for char in chosen_word:
    if char == user_guess:
      list[count] = user_guess
    count += 1
  if user_guess not in chosen_word:
    lives -= 1

  print("\n\n")
  print(list)
  print("\n")
  print(stages[lives])
  print("\n")
  print(f"you have {lives} lives!")
  if lives == 0:
    print("you lo se")
    break
  
  
  if "_" not in list:
    end_game = True

print("\nYou Won")
   
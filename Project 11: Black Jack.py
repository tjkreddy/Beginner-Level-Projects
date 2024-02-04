import random
play_game = True
while play_game == True:
  def print_logo():

    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """
    return logo
  def deal_card():
    ''' this genarates a random card'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card
  
  print(print_logo())
  user_cards = []
  computer_cards = [] 
  exit_game = False
  
  for cards in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  def print_final_results(user_cards, user_cards_sum, computer_cards, computer_cards_sum):
    print(f"Your cards: {user_cards}, final score: {user_cards_sum}")
    print(f"Dealer's card: {computer_cards}, final score: {computer_cards_sum}")
  
  def calculate_sum(cards):
    if sum(cards) == 21 and len(cards) == 2:
      return 0
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
    return sum(cards)
  
  def compare(user_cards_sum, computer_cards_sum):
    if user_cards_sum > 21:
      print("You went over. You lose 😭")
    elif user_cards_sum == computer_cards_sum:
      print("Draw 🙃")
    elif computer_cards_sum == 21:
      print("Lose, Dealer has Blackjack 😱")
    elif user_cards_sum == 21:
      print("Win with a Blackjack 😎")
    elif user_cards_sum > 21:
      print("You went over. You lose 😭")
    elif computer_cards_sum > 21:
      print("Opponent went over. You win 😁")
    else:
      if user_cards_sum > computer_cards_sum:
        print("You win 😃")
      else:
        print("You lose 😤")
  
  while exit_game == False:
    user_cards_sum = calculate_sum(cards = user_cards)
    computer_cards_sum = calculate_sum(cards = computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_cards_sum}")
    print(f"Dealer's first card: {computer_cards[0]}")
  
    if user_cards_sum == 0 or computer_cards_sum == 0 or user_cards_sum > 21:
      exit_game = True
    else:
      extra_card = input("Type 'y' to get another card, type 'n' to pass:\n")
      if extra_card == 'y':
        user_cards.append(deal_card())
      else:
        exit_game = True
  
  while computer_cards_sum != 0 and computer_cards_sum < 17:
    computer_cards.append(deal_card())
    computer_cards_sum = calculate_sum(cards = computer_cards)

  print_final_results(user_cards, user_cards_sum, computer_cards, computer_cards_sum)
  compare(user_cards_sum, computer_cards_sum)

  play_again = input("if do you want play again enter y, if not enter n to exit:\n")
  if play_again == 'n':
    play_game = False



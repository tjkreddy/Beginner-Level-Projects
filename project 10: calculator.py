# from art import logo

logo = """
 _____________________
|  _________________  |
| | PY calculator   | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
 

def addition(num_1, num_2):
  return num_1 + num_2
def subtraction(num_1, num_2):
  return num_1 - num_2
def multiplication(num_1, num_2):
  return num_1 * num_2
def division(num_1, num_2):
  return num_1 / num_2
def print_oper():
  for oper in operator:
    print(oper, end="  ")

operator = {
  "+": addition,
  "-": subtraction,
  "*": multiplication,
  "/": division
}


def calculation():
  print(logo)
  
  num_1 = float(input("enter the first number :\n"))
  again = True
  
  while again:
    print_oper()
    symbol = input("select your operator from above :\n")
    num_2 = float(input("enter the second number :\n"))
    caluclation = operator[symbol]
    answer = caluclation(num_1, num_2)
    print(f" {num_1} {symbol} {num_2} = {answer}")
    loop_again = input(f"Type y to continue with {answer}, type n to contiue with a different number and type exit to exit this code :\n")
    
    if loop_again == "y":
      num_1 = answer
    elif loop_again == "n":
      again = False
      calculation()
    elif loop_again == "exit":
      print("you have exited this code")
      break
    else:
      print("invalid input")
      break


calculation()

# If you give number of letters, numbers and symbols you need in your password as input. 
# then this code will give you a strong password as output


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
for char in range(0,nr_letters):
    random_letter = random.choice(letters)
    password += random_letter
for char in range(0,nr_numbers):
    random_number = random.choice(numbers)
    password += random_number
for char in range(0,nr_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol
random.shuffle(password)                            # to shuffle a list you can use this syntax to do so
final_password=""
for char in password:
    final_password += char            
print(final_password)

 
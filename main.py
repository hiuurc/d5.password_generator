#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

# pick letter
picked_letter = []
for letter in range(nr_letters):
    n_letter = letters[random.randint(1, len(letters) - 1)]
    picked_letter.append(n_letter)

# pick symbols
picked_symbols = []
for symbol in range(nr_symbols):
    n_symbol = symbols[random.randint(1, len(symbols) - 1)]
    picked_symbols.append(n_symbol)

# pick number
picked_number = []
for number in range(nr_numbers):
    n_number = numbers[random.randint(1, len(numbers) - 1)]
    picked_number.append(n_number)

# generate password
list_password = picked_letter + picked_symbols + picked_number
# shuffle
random.shuffle(list_password)
password = "".join(list_password)

print(f'Your password is: {password}')

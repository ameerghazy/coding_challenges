# Password Generator Project

# Importing the random module for generating random characters
import random

# Lists of characters that can be used in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Display a welcome message to the user
print("Welcome to the PyPassword Generator!")

# Prompt the user for the number of letters, symbols, and numbers in the password
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize an empty list to store the generated password
generated_password = []

# Generate random letters based on user input
for char in range(0, nr_letters):
    generated_password += random.choice(letters)
  
# Generate random symbols based on user input
for char in range(0, nr_symbols):
    generated_password += random.choice(symbols)
  
# Generate random numbers based on user input
for char in range(0, nr_numbers):
    generated_password += random.choice(numbers)

# Shuffle the characters in the password to make it random
random.shuffle(generated_password)

# Convert the list of characters into a string
generated_password_strng = ""
for char in generated_password:
    generated_password_strng += char

# Display the generated password to the user
print(f'Your generated password is: {generated_password_strng}')

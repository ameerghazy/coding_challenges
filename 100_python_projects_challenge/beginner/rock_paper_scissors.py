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

# create a list for the images

list = [rock, paper, scissors]

user_input = int(input('What do you choose? Type 0 for rock, 1 for paper or 2 for Scissors.\n'))

# exit if user picks an invalid number

if user_input > 2:
  print("You entered an invalid number")

# print the images for user and computer choices

else:
 computer_choice = random.randint(0,2)

 print(list[user_input])

 print('\nComputer chose:\n')

 print(list[computer_choice])

# check if user wins or ties, otherwise they lose

 if user_input == 0 and computer_choice == 2:
   print('\nYou win!')
  
 elif user_input == 1 and computer_choice == 0:
   print('\nYou win!')
  
 elif user_input == 2 and computer_choice == 1:
   print('\nYou win!')

 elif user_input == computer_choice:
   print('\nYou tie :|')

 else:
   print('\nYou lose :(')

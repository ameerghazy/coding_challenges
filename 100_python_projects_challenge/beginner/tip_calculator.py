# Display a welcome message for the tip calculator program
print('Welcome to the tip calculator.')

# Prompt the user for the total bill amount and convert it to a floating-point number
bill = float(input('What was the total bill? $'))

# Prompt the user for the desired tip percentage (10, 12, or 15) and convert it to an integer
percent_tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))

# Prompt the user for the number of people to split the bill among and convert it to an integer
num_people = int(input('How many people to split the bill? '))

# Calculate the amount of bill per person by dividing the total bill by the number of people
bill_per_person = bill / num_people

# Calculate the amount of tip per person by multiplying the total bill by the tip percentage and then dividing by the number of people
tip_per_person = (bill * (percent_tip / 100)) / num_people

# Calculate the total amount per person, including both bill and tip, and round it to two decimal places
total_per_person = round((bill_per_person + tip_per_person), 2)

# Display the calculated amount each person should pay
print(f'Each person should pay: {total_per_person}')


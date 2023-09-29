# Calculating and displaying travel expenses
# 9/28
# CTI-110 P1HW2 - Travel Expense
# Christen Flores
#
print('This program calculates and displays travel expenses')
budget = int(input('Enter Budget: '))
destination = input('Enter your travel destination: ')
gas = int(input('How much do you think you will spend on gas? '))
accommo = int(input('Approximately, how much will you need for accommodation/hotel? '))
food = int(input('Last, how much do you need for food? '))
print('------------Travel Expenses----------')
print('Location: ', destination)
print('Initial Budget: ', budget)
print()
print('Fuel: ', gas)
print('Accommodation: ', accommo)
print('Food: ', food)
print()
print('Remaining Balance: ', budget-gas-accommo-food)

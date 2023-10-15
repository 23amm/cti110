# Creating cleaner looking results
# 10/15
# CTI-110 P2HW1 - Travel
# Christen Flores
#
#More space for easier reading
#Change int's to floats
print('This program calculates and displays travel expenses')
print()
budget = float(input('Enter Budget: '))
print()
destination = input('Enter your travel destination: ')
print()
gas = float(input('How much do you think you will spend on gas? '))
print()
accommo = float(input('Approximately, how much will you need for accommodation/hotel? '))
print()
food = float(input('Last, how much do you need for food? '))
#Make results tighter and aligned
#Add '$' to expenses
print()
print('------------Travel Expenses----------')
print('Location:          ',(destination))
print('Initial Budget:     $'+ str(budget))
print('Fuel:               $'+ str(gas))
print('Accommodation:      $'+ str(accommo))
print('Food:               $'+ str(food))
print('-------------------------------------')
print()
print('Remaining Balance:  $'+ str(budget-gas-accommo-food))

# CTI-110
# P2HW2 - List
# Christen Flores
# 10/15
#
# Create inputs for the user's grades in each module

Module_1 = float(input('Enter grade for Module 1: '))
Module_2 = float(input('Enter grade for Module 2: '))
Module_3 = float(input('Enter grade for Module 3: '))
Module_4 = float(input('Enter grade for Module 4: '))
Module_5 = float(input('Enter grade for Module 5: '))
Module_6 = float(input('Enter grade for Module 6: '))
print()

#list of grades

Module_Grades = [Module_1,Module_2,Module_3,Module_4,Module_5,Module_6]

#Results in order of min, max, sum, average

print('------------Results------------')
print(f'{"Lowest Grade:":<20}{min(Module_Grades):<10}')
print(f'{"Highest Grade:":<20}{max(Module_Grades):<10}')
print(f'{"Sum of Grades:":<20}{sum(Module_Grades):<10}')

average = (Module_1 + Module_2 + Module_3 + Module_4 + Module_5 + Module_6) / 6

print(f'{"Average:":<20}{average:<10.2f}')
print('-------------------------------------------')

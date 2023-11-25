# Math Quiz Program
# 11/25/2023
# CTI-110 P5HW - Math Quiz
# Christen Flores

import random

def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def add_numbers():
    num1, num2 = generate_numbers()
    print(" ", num1)
    print("+", num2)
    print()
    correct_answer = num1 + num2
    return correct_answer

def subtract_numbers():
    num1, num2 = generate_numbers()
    print(" ", num1)
    print("-", num2)
    print()
    correct_answer = num1 - num2
    return correct_answer

def math_quiz():
    while True:
        print("MAIN MENU")
        print("-------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        print()
        
        choice = input("Please choose one of the menu options: ")
        
        if choice == '1':
            correct_answer = add_numbers()
        elif choice == '2':
            correct_answer = subtract_numbers()
        elif choice == '3':
            print("Thank you for playing...")
            print("Bye!!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
        
        attempts = 0
        while True:
            if attempts == 0:
                print("Enter answer.")
            else:
                print("Try again:", end=" ")
                
            user_answer = int(input())
            attempts += 1
            
            if user_answer == correct_answer:
                print("Congratulations!!!! Your answer is correct.")
                print("Number of guesses:", attempts)
                print()
                break
            elif user_answer < correct_answer:
                print("Sorry, guess is too low.")
                print()
            else:
                print("Sorry, guess is too high.")
                print()

if __name__ == "__main__":
    math_quiz()


# print("Hello from lesson 9")

"""
# Task 1

num1 = int(input("Enter a number: "))

if num1 > 0:
    print(f"{num1} is positive.")
else:
    print(f"{num1} is negative.")
"""

"""
# Task 2

import random

ran_num = random.randint(1, 10)
print(ran_num)

guess = int(input("Guess the number: "))

if guess == ran_num:
    print("Congratulations! You did it!")
else:
    print("Oops, better luck next time.")
"""

"""
# Task 3

pw = "C@deForFun"

login = input("Enter the password: ")

if login == pw:
    print("Login Successful")
else:
    print("Invalid Password")
"""

"""
# Task 4

num1 = int(input("Enter a number: "))

if num1 % 2 == 0:
    print(f"{num1} is an even number.")
else:
    print(f"{num1} is an odd number.")
"""

"""
# Task 5

user_age = int(input("Enter your age: "))

if user_age < 13:
    print("Child")
elif user_age >= 13 and user_age <= 19:
    print("Teen")
else:
    print("Adult")
"""

"""
# Task 6

temp = int(input("Enter the temperature: "))

if temp < 20:
    print("Consider reading indoors.")
elif temp >= 20 and temp <= 30:
    print("It is a great day for cycling.")
else:
    print("How about a swimming session?")
"""

# Task 7a

import random

ran_num = random.randint(1, 10)
print(ran_num)

guess = int(input("Guess the number: "))

if ran_num > guess:
    print("Higher!")
else:
    if ran_num < guess:
        print("Lower!")
    else:
        if ran_num == guess:
            print("You got it!")
        else:
            print("Invalid input!")

# Task 7b

import random

ran_num = random.randint(1, 10)
print(ran_num)

guess = int(input("Guess the number: "))

if ran_num > guess:
    print("Higher!")
else:
    if ran_num < guess:
        print("Lower!")
    else:
        if ran_num == guess:
            print("You got it!")
        else:
            print("Invalid input!")






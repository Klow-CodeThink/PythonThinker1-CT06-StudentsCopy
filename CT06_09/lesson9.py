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


# Task 3

pw = "C@deForFun"

login = input("Enter the password: ")

if login == pw:
    print("Login Successful")
else:
    print("Invalid Password")

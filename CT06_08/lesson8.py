# print("Hello from lesson 8")

"""
# Task 1a

import time

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
"""

"""
# Task 1b

import time

count_start = int(input("Enter start countdown: "))

for i in range(count_start, 0, -1):
    print(i)
    time.sleep(1)
"""

"""
# Task 2a

import random
print(random.randint(1, 6))
"""

"""
# Task 2b

import random

for i in range (20):
    print(f"Random Number {str(i+1)}: {random.randint(0, 9999)}")
"""

"""
# Task 3a

is_sunny = True     # Assign a Boolean value

print(is_sunny)     # Print the value
"""

"""
# Task 3b

value1 = 10               # Create two Boolean variables
value2 = 10

result = value1 == value2   # Compare using ==

print(f"Are the two values equal? {result}") # Print the result
"""

"""
# Task 3c

a = 10
b = 5

# Comparison results are Boolean
print(f"Is a greater than b? {a > b}")     # True
print(f"Is a equal to b? {a == b}")        # False
"""

"""
# Task 4a

import random

a = random.randint(1, 50)
b = random.randint(1, 50)

ans = int(input(f"What is {a} + {b}? "))

result = ans == (a + b)

print(result)
"""

"""
# Task 4b

import random

com_ran = random.randint(1, 50)

print(com_ran)

user_start = int(input("Enter the start number: "))
user_end = int(input("Enter the end number: "))

result = com_ran > user_start and com_ran < user_end

print(result)
"""

"""
# Task 5

import random

num1 = random.randint(1, 10)

print(num1)

guess = int(input("Guess My Number: "))

result = guess == num1

print(result)
"""

"""
# Task 6

import random

num_ques = int(input("How many multiplication questions would you like? "))

for i in range(num_ques):
    first_num = random.randint(1, 10)           # Loop through the number of questions
    second_num = random.randint(1, 10)
    
    ans = int(input(f"What is {first_num} x {second_num}? "))
    
    result = ans == (first_num * second_num)
    
    print(result)
"""

"""
# Task 7

import random

num1 = int(input("Enter a number: "))

even_num = num1 % 2 == 0

print(f"Is your number an even number? {even_num}")
"""

"""
# Task 8

import random

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

mul_num = num1 % num2 == 0

print(f"{num1} is a multiple of {num2}. {mul_num}")
"""

"""
# Challenge 1

score = 0

import time

print("Welcome to Whiz Quiz Game!")
time.sleep(2)
print("You will be tested on 3 General Knowledge questions.")
time.sleep(2)
print("Let's start!")
time.sleep(2)
Q1 = input("Question 1: What is the capital of France? ")

print(f"Your answer: {Q1}")

if Q1 == "Paris":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect. The correct answer is Paris.")

time.sleep(2)
Q2 = input("Question 2: Who wrote 'To Kill A Mockingbird? ")

print(f"Your answer: {Q2}")

if Q2 == "Harper Lee":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect. The correct answer was Harper Lee.")


time.sleep(2)
Q3 = input("Question 3: What is the smallest planet in our solar system? ")

print(f"Your answer: {Q3}")

if Q3 == "Mercury":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect. The correct answer is Mercury.")

print(f"Whiz Quiz is completed. Your final score is {score}/3.")
"""


# Challenge 2

import random

ran_num = random.randint(1, 100)
print(ran_num)

print("Guess the number between 1 and 100. You have 5 attempts.")
time.sleep(2)

for i in range(5):
    G1 = int(input("Enter your guess: "))
    print("Attempt ")








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


"""
# Task 1a

visitors = 0

while visitors < 50:
    visitors = visitors + 1     # visitors += 1
    print(visitors)
"""

"""
# Task 1b

visitors = 18

while visitors < 30:
    visitors = visitors + 1     # visitors += 1
    print(visitors)
"""

"""
# Task 1c

visitors = 4

while visitors < 25:
    visitors = visitors + 1     # visitors += 1
    print(visitors)
"""

"""
# Task 2

visitors = 0

while True:
    visitors += 1
    print(visitors)
    if visitors == 30:
        break
"""

"""
# Task 3

order = " "

while True:
    plc_order = input("What would you like to order (type 'end' to finish): ").lower()
    if plc_order == "end":
        break
    order = order + plc_order + " "

print(f"You have ordered: {order}")
"""

"""
# Task 4a

count = 10

while count > 0:
    print(count)
    count -= 1
else:
    print("Happy New Year!")
"""

"""
# Task 4b

count = 10

while count > 0:
    print(count)
    
    if count == 5:
        break
    else:
        count -= 1
"""

"""
# Task 5a

import random

while True:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    ques = int(input(f"What is {num1} x {num2}? "))
    if ques == (num1 * num2):
        print("That's correct.")
        break
    else:
        print("Wrong. Try again.")
"""

"""
# Task 5b

import random

score = 0

while score < 5:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    ques = int(input(f"What is {num1} x {num2}? "))
    if ques == (num1 * num2):
        score = score + 1
        print("That's correct.")
    else:
        print("Wrong. Try again.")

print("You got 5 correct answers! Well done!")
"""


# Task 6

import random

number = 0
while number != 4:
    number = random.randint(1, 6)
    print("Rolled:", number)



# import random

# while True:
#     number = random.randint(1, 6)
#     print("Rolled:", number)

#     if number == 4:
#         print("It's a 4! Stopping.")
#         break







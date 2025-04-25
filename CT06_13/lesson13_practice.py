
"""
# Task 1a

shoplist = []

shoplist.append("apples")
shoplist.append("bread")
shoplist.append("carrots")
shoplist.append("dates")
shoplist.append("eggs")
shoplist.append("flour")
shoplist.append("grapes")
shoplist.append("honey")

# print(shoplist)


# Task 1b

shoplist[7] = "herbs"

# print(shoplist)


# Task 1c

shoplist.append("ice")
shoplist.insert(1, "bananas")

# print(shoplist)


# Task 1d

del(shoplist[2])

# print(shoplist)



# Task 2

for groceries in shoplist:
    print(groceries)
"""

"""
grocery = "Apples"

if grocery == "Apples":
    print(f"{grocery}: I need 5 of these")


grocery = "Carrots"

if grocery == "Carrots":
    print(f"{grocery}: I need 3 of these")


grocery = "Grapes"

if grocery == "Grapes":
    print(f"{grocery}: Get the FarmFresh brand")
"""

"""
# Task 3

basket = []

while True:
    item = input("What item have you added to your basket? ").lower()

    if item == "end":
        break

    basket.append(item)

# Print each item in the required format
for grocery in basket:
    print(f"I have bought {grocery}.")
"""

"""
# Task 4a

catalogue = []

while True:
    item = input("Enter an item to add to the catalogue: ").lower()

    if item == "end":
        break

    catalogue.append(item)

# Display the final catalogue
print("Online Grocery Catalogue:")
for product in catalogue:
    print(f"- {product}")

# or

catalogue = []

print("Create your online grocery catalogue.")
print("Type 'end' when you're finished.\n")

while True:
    item = input("Enter an item to add to the catalogue: ").strip()

    if item.lower() == "end":
        break

    catalogue.append(item)
    print(f"'{item}' has been added to the catalogue.\n")

# Display the final catalogue
print("\n🛒 Online Grocery Catalogue:")
for product in catalogue:
    print(f"- {product}")
"""

"""
# Task 4b

catalogue = []

while True:
    item = input("Enter an item to add to the catalogue: ").strip().lower()

    if item == "end":
        break

    catalogue.append(item)
    print(f"'{item}' has been added to the catalogue.\n")

# Step 2: Ask the user what they're looking for
search = input("What are you looking for? ").strip().lower()

# Step 3: Check if the item is in the catalogue
if search in catalogue:
    print("Yes, we sell that.")
else:
    print("I'm sorry. We do not have that.")
"""

"""
# Task 5

import random

lucky_draw_numbers = []

for _ in range(10):
    number = random.randint(1, 9999)
    lucky_draw_numbers.append(number)

for i in range(len(lucky_draw_numbers)):
    print(f"Winner #{i + 1}: {lucky_draw_numbers[i]}")
"""

"""
# Task 6

# Step 1: List of available toppings
toppings = ["pepperoni", "mushrooms", "onions", "sausage", "extra cheese"]

# Step 2: Show toppings with index numbers
print("Available pizza toppings:")
for i in range(len(toppings)):
    print(f"{i}: {toppings[i]}")

# Step 3: Ask user to select toppings by index
selected_toppings = []

while True:
    choice = input("\nWhich topping would you like? (Enter index or type 'end' to finish): ").strip().lower()

    if choice == "end":
        break

    if choice.isdigit():
        index = int(choice)
        if 0 <= index < len(toppings):
            selected_toppings.append(toppings[index])
            print(f"Added {toppings[index]} to your pizza.")
        else:
            print("Invalid index. Please choose a number from the list.")
    else:
        print("Please enter a valid number or 'end'.")

# Step 4: Print the selected toppings
print("\n🍕 You have selected the following toppings:")
for topping in selected_toppings:
    print(f"- {topping}")
"""








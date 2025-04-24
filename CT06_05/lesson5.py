print("Hello from lesson 5")

# Ask for the total number of students
num_students = int(input("Enter the number of students: "))

# Initialize a total variable to store the sum of marks
total_marks = 0

# Use a for loop to ask for each student's mark
for i in range(1, num_students + 1):
    mark = float(input("Enter mark for student " + str(i) + ": "))
    total_marks += mark  # Add the mark to the total

# Calculate the average
average = total_marks / num_students

# Display the average
print("The average mark is:", round(average, 2))
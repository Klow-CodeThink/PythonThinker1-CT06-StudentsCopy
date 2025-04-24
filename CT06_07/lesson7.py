# print("Hello from lesson 7")

num_stu = int(input("Enter the number of students: "))

thesum = 0

for i in range(1, num_stu + 1):
    score = int(input("What is the score for Student " + str(i+1) + " ? "))
    thesum = thesum + score

print(f"The average score is ({thesum / num_stu}.")
















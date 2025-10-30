# lesson_3_conditionals_loops.py
# Author: Bhumi Gowda
# Lesson 3: Conditionals & Loops

# --- Conditional Statements ---
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+ 🏆 Excellent!")
elif marks >= 75:
    print("Grade: A 🎯 Great job!")
elif marks >= 60:
    print("Grade: B 👍 Keep improving!")
elif marks >= 40:
    print("Grade: C ⚡ You passed!")
else:
    print("Grade: F 😔 Try again!")

# --- For Loop ---
print("\nCounting from 1 to 5 using for loop:")
for i in range(1, 6):
    print(i)

# --- While Loop ---
print("\nWhile loop countdown:")
count = 5
while count > 0:
    print(count)
    count -= 1

print("Liftoff! 🚀")

# --- Task for You ---
# 1️⃣ Take an integer input from the user.

n = int(input("Enter an integer : "))
# 2️⃣ If the number is even, print all even numbers up to that number.

if(n%2 == 0):
    for i in range (n):
        if(i%2 == 0):
            print(i)
# 3️⃣ If it’s odd, print all odd numbers up to that number.

else:
    for i in range(n):
        if(i%2!=0):
            print(i)

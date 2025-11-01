# lesson_1_basics.py
# Author: Bhumi Gowda
# Lesson 1: Python Fundamentals

# --- Variables and Data Types ---
name = "Bhumi"
age = 19
cgpa = 8.7
is_student = True

print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Student:", is_student)

# --- Input and Output ---
user_name = input("\nEnter your name: ")
print("Hello,", user_name, "! Welcome to your GSoC 2027 journey 🚀")

# --- Operators ---
a = 10
b = 3
print("\nBasic Math Operations:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("\n")
# --- Task for You ---
# 1️⃣ Take marks of 3 subjects as input

m1 = float(input("Enter marks for subject 1 : "))
m2 = float(input("Enter marks for subject 2 : "))
m3 = float(input("Enter marks for subject 3 : "))
print("\n")
# 2️⃣ Calculate average

avg = (m1+m2+m3)/3

# 3️⃣ If avg >= 40, print "Pass" else "Fail"

if(avg>=40):
    print("you have Passed")
else:
    print("you have Failed")
# lesson_2_strings_lists.py
# Author: Bhumi Gowda
# Lesson 2: Strings & Lists in Python

# --- Strings ---
quote = "Success doesn’t come overnight"
print("Original Quote:", quote)
print("Uppercase:", quote.upper())
print("Lowercase:", quote.lower())
print("Split Words:", quote.split())
print("First 7 letters:", quote[:7])
print("Last 5 letters:", quote[-5:])

# --- Concatenation ---
name = "Bhumi"
goal = "GSoC 2027"
message = name + " is preparing for " + goal
print("\nMessage:", message)

# --- Lists ---
friends = ["Anu", "Riya", "Kiran", "Manu"]
print("\nMy Friends List:", friends)
print("First friend:", friends[0])
print("Last friend:", friends[-1])

# Add and remove elements
friends.append("Sahana")
friends.remove("Riya")
print("Updated List:", friends)

# --- Looping through list ---
print("\nFriend names one by one:")
for friend in friends:
    print(friend)

# --- Task for You ---
# Create a list of your 5 favorite AI tools.

ai_tools = ["ChatGPT", "TensorFlow", "PyTorch", "Keras", "OpenAI Codex"]
# Print each with a message like:
for i in range(len(ai_tools)):
    print(f"Tool {i+1} : {ai_tools[i]}")
# "Tool 1: ChatGPT", "Tool 2: TensorFlow", etc.

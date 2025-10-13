# -------------------------------------------
# Exercise 2: While Loops
# -------------------------------------------
# In this exercise, you’ll work in groups of 2–3.
# You’ll learn how to repeat code using a while loop.
# A while loop runs *while a condition is True*.
#
# Syntax reminder:
# while condition:
#     # code that repeats
#
# Example (syntax only):
# count = 0
# while count < 5:
#     print("Repeating...")
#     count = count + 1
#
# -------------------------------------------
# GROUP INSTRUCTIONS
# -------------------------------------------
# Work in groups of 2–3 learners.
# You will all share the same GitHub Classroom repository.
#
# After each task:
# - The learner who is currently coding will git add, commit, and push.
# - The next learner will move to their own computer, git pull, and continue.
#
# If you are in pairs:
# - Swap computers after each task (back and forth).
# -------------------------------------------


# Task 1: Simple Counting Loop
# -------------------------------------------
# A while loop repeats until a condition becomes False.
#
# TODO:
# 1. Create a variable called count and set it to 1.
# 2. Write a while loop that runs while count is less than or equal to 5.
# 3. Print the value of count each time the loop runs.
# 4. Add 1 to count inside the loop so it eventually stops.
#
# Example (similar idea):
# while number < 3:
#     print("Loop running")
#     number = number + 1
#
# Write your code below:


# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex2_while_loops.py
#    git commit -m "Completed Task 1 - counting loop"
#    git push origin main
# 4. The next learner goes to their own computer.
# 5. On their computer, open the terminal and run:
#    git pull
# -------------------------------------------


# Task 2: Using While with User Input
# -------------------------------------------
# You can control loops with user input.
#
# TODO:
# 1. Ask the user to type a word.
# 2. Keep asking them until they type "stop".
# 3. Each time, print a message like "You typed <word>".
#
# Example (similar idea):
# while something != "quit":
#     print("You typed something")
#     something = input("Type again: ")
#
# Write your code below:


# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex2_while_loops.py
#    git commit -m "Completed Task 2 - while with input"
#    git push origin main
# 4. The next learner goes to their own computer.
# 5. On their computer, open the terminal and run:
#    git pull
# -------------------------------------------


# Task 3: While Loop with Numbers
# -------------------------------------------
# TODO:
# 1. Ask the user to enter a number between 1 and 10.
# 2. Keep asking until they actually give a number in that range.
# 3. When they finally do, print a thank-you message.
#
# Hint: You’ll need to use int() to convert the input into a number.
# Example (similar idea):
# while guess != target:
#     print("Try again")
#
# Write your code below:


# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex2_while_loops.py
#    git commit -m "Completed Task 3 - number validation"
#    git push origin main
# 4. The next learner goes to their own computer.
# 5. On their computer, open the terminal and run:
#    git pull
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------
# Now that everyone has had a turn, continue swapping computers
# after each extension task as before.
# -------------------------------------------

# Extension 1:
# -------------------------------------------
# Create a simple counter that counts down from 10 to 1.
# Print each number.
# When it finishes, print "Liftoff!"
#
# Example (similar idea):
# while something > 0:
#     print(something)
#     something = something - 1

# Write your code below:


# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save and push this file:
#    git add Ex2_while_loops.py
#    git commit -m "Completed Extension 1 - countdown"
#    git push origin main
# 2. Next learner: git pull
# -------------------------------------------


# Extension 2:
# -------------------------------------------
# Ask the user to enter a password.
# Keep asking until they type the correct one.
# When they get it right, print “Access granted”.
#
# Hint: You can compare strings using ==.
# Example (similar idea):
# while password_entered != correct_password:
#     print("Try again")

# Write your code below:


# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save and push this file:
#    git add Ex2_while_loops.py
#    git commit -m "Completed Extension 2 - password loop"
#    git push origin main
# 2. Next learner: git pull
# -------------------------------------------


# Extension 3:
# -------------------------------------------
# Ask the user to enter numbers.
# Keep adding them together into a total.
# When the total goes above 50, stop the loop and print the total.
#
# Example (similar idea):
# while total < 100:
#     num = int(input("Enter a number: "))
#     total = total + num

# Write your code below:


# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save and push this file:
#    git add Ex2_while_loops.py
#    git commit -m "Completed Extension 3 - total sum loop"
#    git push origin main
# 2. Next learner: git pull
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY
# -------------------------------------------
# Now complete this challenge together.
# Choose one learner’s computer to finish on (the last one used is fine).
#
# Advanced Task:
# Create a number guessing game.
# 1. Set a secret number (e.g. 7).
# 2. Ask the user to guess the number.
# 3. Use a while loop to keep asking until they guess correctly.
# 4. If the guess is too high or too low, print a hint.
# 5. When correct, print how many tries it took.
#
# Hint: Use a counter variable to count attempts.

# Write your code below:


# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you’ve completed this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex2_while_loops.py
#    git commit -m "Completed advanced while loop activity"
#    git push origin main
# 4. Check GitHub to confirm your group’s final version appears.
# -------------------------------------------

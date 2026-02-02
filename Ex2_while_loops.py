# -------------------------------------------
# Exercise 2: While Loops
# -------------------------------------------
#
# GOAL:
# 1. Master Repetition based on conditions (While loops).
# 2. Practise the "Relay Race" Git workflow in groups of 2-3.
#
# CONCEPT:
# A 'while' loop is like a repeating 'if' statement.
# It continues to run the code block *while* a condition remains True.
# - Useful when you don't know exactly how many times you need to loop
#   (e.g., waiting for a user to type the correct password).
#
# PAIR PROGRAMMING RULES:
# - The DRIVER types the code.
# - The NAVIGATOR guides the driver.
# - You will SWITCH roles and computers after every task!
# -------------------------------------------


# -------------------------------------------
# Task 1: The Counter
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: The Counter\n"
    + "-------------------------------------------")

# TODO:
# 1. Create a variable called 'count' and set it to 1.
# 2. Write a while loop that runs while 'count' is less than or equal to 5.
# 3. Inside the loop:
#    - Print the value of 'count'.
#    - Add 1 to 'count' (count = count + 1).
#
# Warning: If you forget to add 1, you will create an "Infinite Loop"!

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file (Ctrl+S).
# 2. Open the terminal.
# 3. Run:
#    git add Ex2_while_loops.py
#    git commit -m "Completed Task 1"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# Task 2: The Parrot (User Input)
# -------------------------------------------
# INSTRUCTION: You are now at a new computer.
# 1. Open the terminal.
# 2. Run: `git pull origin main`

print("\n-------------------------------------------\n"
    + "Task 2: The Parrot\n"
    + "-------------------------------------------")

# TODO:
# 1. Create a variable called 'user_word' and set it to an empty string "" or "start".
# 2. Create a while loop that runs while 'user_word' is NOT equal to "stop".
# 3. Inside the loop:
#    - Ask the user to type a word (Input).
#    - Print "You typed: " followed by their word.
#
# Note: The loop should only end when they type "stop".

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex2_while_loops.py
#    git commit -m "Completed Task 2"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# Task 3: The Gatekeeper (Validation)
# -------------------------------------------
# INSTRUCTION: Get the code from the previous Driver.
# 1. Run: `git pull origin main`

print("\n-------------------------------------------\n"
    + "Task 3: The Gatekeeper\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user to enter a number (convert to int) and store it in a variable.
# 2. Create a while loop that runs while the number is LESS than 1 OR GREATER than 10.
# 3. Inside the loop:
#    - Print "Invalid number. Try again."
#    - Ask for the number again (update the variable).
# 4. Outside the loop (after it finishes), print "Thank you!".

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex2_while_loops.py
#    git commit -m "Completed Task 3"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: The Rocket Launch
# -------------------------------------------
# INSTRUCTION: Run `git pull origin main` first.

print("\n-------------------------------------------\n"
    + "Extension 1: The Rocket Launch\n"
    + "-------------------------------------------")

# TODO:
# 1. Create a variable set to 10.
# 2. Loop while the variable is greater than 0.
# 3. Print the number, then subtract 1 from the variable.
# 4. When the loop finishes, print "Liftoff!".

# Write your code below:


# Extension 2: The Security System
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 2: The Security System\n"
    + "-------------------------------------------")

# TODO:
# 1. Create a variable 'correct_pass' = "python123".
# 2. Ask the user to enter a password.
# 3. While the input does NOT match 'correct_pass':
#    - Print "Access Denied."
#    - Ask for the password again.
# 4. Print "Access Granted" when the loop ends.

# Write your code below:


# Extension 3: The Accumulator
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 3: The Accumulator\n"
    + "-------------------------------------------")

# TODO:
# 1. Create a variable 'total' and set it to 0.
# 2. Loop while 'total' is less than or equal to 50.
# 3. Ask the user for a number (integer).
# 4. Add that number to 'total'.
# 5. Print the current total inside the loop.
# 6. When the loop breaks (total > 50), print "Limit reached!".

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex2_while_loops.py
#    git commit -m "Completed extensions"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY: The Hi-Lo Game
# -------------------------------------------
# INSTRUCTION: Run `git pull origin main` first.

print("\n-------------------------------------------\n"
    + "ADVANCED ACTIVITY: The Hi-Lo Game\n"
    + "-------------------------------------------")

# TODO:
# 1. Set a secret number (e.g. 7).
# 2. Create a variable 'tries' set to 0.
# 3. Create a variable 'guess' set to 0.
# 4. Loop while 'guess' is NOT equal to the secret number:
#    - Ask the user to guess.
#    - Add 1 to 'tries'.
#    - IF guess > secret: Print "Too high!"
#    - ELIF guess < secret: Print "Too low!"
# 5. Print f"Correct! It took you {tries} tries."

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save this file.
# 2. Run:
#    git add Ex2_while_loops.py
#    git commit -m "Completed Hi-Lo game"
#    git push origin main
# -------------------------------------------

# ============================================================
# LESSON 1: Variables and Data Types
# ============================================================
# In programming, a VARIABLE is like a labelled box that stores
# a value. You create one by choosing a name and using = to
# assign a value to it.
#
# Python has several basic data types:
#   - str   (text)      → written in quotes: "hello"
#   - int   (whole number)  → written without quotes: 42
#   - float (decimal number) → written with a dot: 3.14
#   - bool  (True/False)    → written as: True or False
# ============================================================

# --- STRINGS (str) ---
# A string is text. Always wrapped in quotes (single or double).
name = "Chris"
greeting = "Hello"
print(greeting + ", " + name + "!")   # Joining strings with + is called "concatenation"

# --- INTEGERS (int) ---
# An integer is a whole number (no decimal point).
age = 30
days_in_year = 365
print("Age: " + str(age))            # str() converts a number to text so we can join it

# --- FLOATS (float) ---
# A float is a number with a decimal point.
height = 1.75
pi = 3.14159
print("Pi is approximately: " + str(pi))

# --- BOOLEANS (bool) ---
# A boolean is either True or False. Used for yes/no decisions.
is_learning_python = True
is_expert_yet = False
print("Currently learning Python: " + str(is_learning_python))

# --- BASIC MATHS ---
# Python can do maths with numbers:
#   +  add
#   -  subtract
#   *  multiply
#   /  divide
#   ** power (e.g. 2**3 = 8)
a = 10
b = 3
print("10 + 3  =", a + b)       # Note: print() can take multiple values separated by commas
print("10 - 3  =", a - b)
print("10 * 3  =", a * b)
print("10 / 3  =", a / b)       # Division always gives a float
print("10 ** 3 =", a ** b)      # 10 to the power of 3

# --- CHECKING TYPES ---
# type() tells you what kind of data a variable holds.
print(type(name))                # <class 'str'>
print(type(age))                 # <class 'int'>
print(type(height))              # <class 'float'>
print(type(is_learning_python))  # <class 'bool'>


# ============================================================
# YOUR TASKS (try these yourself!):
# ============================================================
#

# TASK 1: Create a variable called "favourite_food" and set it
#         to your favourite food. Then print it.
#         Example: favourite_food = "pizza"
favourite_food = "ice cream"
print("My favourite food is " + favourite_food)

# TASK 2: Create two number variables called "x" and "y",
#         give them any values, and print their sum, difference,
#         and product.
#         Hint: use print("Sum:", x + y)
#



# TASK 3: Create a variable called "birth_year" (int), and use
#         maths to calculate your age from it. Print the result.
#         Hint: age = 2026 - birth_year
#
# TASK 4: What happens if you try to do this:
#             print("My age is " + 25)
#         Try it! Read the error message. Then fix it using str().
#
# ============================================================
# When you've completed the tasks, tell me and I'll review
# your code and move on to Lesson 2: User Input & f-strings!
# ============================================================

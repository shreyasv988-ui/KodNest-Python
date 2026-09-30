# =====================================================================
# KodNest Python Track - Module 02: Data Structures (Strings)
# Topic: Built-in String Methods
# =====================================================================

# ---------------------------------------------------------------------
# 1. Case Conversion Methods
# ---------------------------------------------------------------------
text = "hello KodNest python"

print("--- 1. Case Conversion Methods ---")
print("Original text:      ", text)
print("text.upper():       ", text.upper())       # Converts all characters to uppercase
print("text.lower():       ", text.lower())       # Converts all characters to lowercase
print("text.title():       ", text.title())       # Capitalizes first letter of each word
print("text.capitalize():  ", text.capitalize())  # Capitalizes only the first letter of string
print("text.swapcase():    ", text.swapcase())    # Inverts lower to upper and upper to lower
print()

# ---------------------------------------------------------------------
# 2. Search and Count Methods
# ---------------------------------------------------------------------
msg = "Python is awesome, Python is simple"

print("--- 2. Search & Count Methods ---")
print("msg.count('Python'):  ", msg.count("Python"))  # Counts occurrences of substring (2)
print("msg.find('is'):        ", msg.find("is"))        # First index where found (7)
print("msg.rfind('is'):       ", msg.rfind("is"))       # Last index where found (26)
print("msg.find('Java'):      ", msg.find("Java"))      # Returns -1 if not found
print("msg.index('is'):       ", msg.index("is"))       # Similar to find(), but raises ValueError if not found
print("msg.startswith('Py'):  ", msg.startswith("Py"))  # True
print("msg.endswith('ple'):   ", msg.endswith("ple"))   # True
print()

# ---------------------------------------------------------------------
# 3. Trimming / Stripping Whitespace & Characters
# ---------------------------------------------------------------------
padded_str = "   KodNest Python   "

print("--- 3. Trimming Methods ---")
print("Original:       '", padded_str, "'", sep="")
print("strip():        '", padded_str.strip(), "'", sep="")    # Removes leading & trailing whitespace
print("lstrip():       '", padded_str.lstrip(), "'", sep="")   # Removes leading (left) whitespace
print("rstrip():       '", padded_str.rstrip(), "'", sep="")   # Removes trailing (right) whitespace

custom_strip = "###Welcome to KodNest###"
print("Custom strip:   ", custom_strip.strip("#"))             # Removes specific characters
print()

# ---------------------------------------------------------------------
# 4. Splitting and Joining Strings
# ---------------------------------------------------------------------
print("--- 4. Splitting and Joining ---")
sentence = "Java,Python,SQL,HTML"
languages = sentence.split(",")  # Splits string into a list using delimiter
print("sentence.split(','):  ", languages)

# Joining list elements into a single string
joined_text = " - ".join(languages)
print("'-'.join(languages):   ", joined_text)
print()

# ---------------------------------------------------------------------
# 5. Replacement and Transformation
# ---------------------------------------------------------------------
print("--- 5. Replacement ---")
course = "I am learning Java at KodNest"
new_course = course.replace("Java", "Python")  # Replaces 'Java' with 'Python'
print("Original:   ", course)
print("Replaced:   ", new_course)
print()

# ---------------------------------------------------------------------
# 6. Checking / Validation Methods (Boolean return values)
# ---------------------------------------------------------------------
print("--- 6. Validation (is*) Methods ---")
alpha = "KodNest"
num = "12345"
alnum = "KodNest2026"
space = "   "

print(f"'{alpha}'.isalpha():  ", alpha.isalpha())   # True (letters only)
print(f"'{num}'.isdigit():    ", num.isdigit())     # True (digits only)
print(f"'{alnum}'.isalnum():  ", alnum.isalnum())   # True (letters and digits)
print(f"'{space}'.isspace():  ", space.isspace())   # True (spaces only)
print(f"'HELLO'.isupper():    ", "HELLO".isupper()) # True (all uppercase)
print(f"'hello'.islower():    ", "hello".islower()) # True (all lowercase)
print(f"'Title'.istitle():    ", "Title".istitle()) # True (title case)
print()

# ---------------------------------------------------------------------
# 7. Alignment and Padding
# ---------------------------------------------------------------------
print("--- 7. Alignment & Padding ---")
word = "KodNest"
print("word.center(20, '*'): ", word.center(20, "*")) # Centered with fill character
print("word.ljust(20, '-'):  ", word.ljust(20, "-"))  # Left aligned
print("word.rjust(20, '-'):  ", word.rjust(20, "-"))  # Right aligned
print("'42'.zfill(5):        ", "42".zfill(5))        # Zero fill to 5 digits: 00042


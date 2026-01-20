#1. Validates a strong password using regular expressions with the following rules:
	#Minimum 8 characters
	#At least one uppercase letter
	#At least one lowercase letter
	#At least one digit
	#At least one special character

import re


def is_strong_password(password):
    """
    Validates whether the given password is strong.
    """
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    if re.match(pattern, password):
        return True
    return False


# Input
password = input("Enter your password: ")

# Output
if is_strong_password(password):
    print("Strong Password")
else:
    print("Weak Password")

#2. Uses lookahead assertions (?=)
import re

def validate_password(password):
    """
    Validates a strong password using lookahead assertions.
    """
    regex = (
        r'^(?=.*[A-Z])'      # at least one uppercase letter
        r'(?=.*[a-z])'       # at least one lowercase letter
        r'(?=.*\d)'          # at least one digit
        r'(?=.*[@$!%*?&])'   # at least one special character
        r'.{8,}$'            # minimum 8 characters
    )

    return bool(re.match(regex, password))


# Input
password = input("Enter password: ")

# Output
if validate_password(password):
    print("Strong Password")
else:
    print("Weak Password")

#3. Uses regular expression modifiers such as:
#re.IGNORECASE
#re.MULTILINE
#re.DOTALL
import re

text = "Hello\nWORLD\nPython"

print("Original Text:")
print(text)
print("-" * 40)

# 1. re.IGNORECASE
print("1. Using re.IGNORECASE")
pattern = "world"
match = re.search(pattern, text, re.IGNORECASE)
print("Pattern:", pattern)
print("Match found:", bool(match))
print("-" * 40)

# 2. re.MULTILINE
print("2. Using re.MULTILINE")
pattern = "^WORLD"
match = re.search(pattern, text, re.MULTILINE)
print("Pattern:", pattern)
print("Match found:", bool(match))
print("-" * 40)

# 3. re.DOTALL
print("3. Using re.DOTALL")
pattern = "Hello.*Python"
match = re.search(pattern, text, re.DOTALL)
print("Pattern:", pattern)
print("Match found:", bool(match))
print("-" * 40)


#4. Demonstrates how modifiers affect pattern matching with examples
# 4. Without modifiers (comparison)
print("4. Without modifiers (comparison)")
pattern = "Hello.*Python"
match = re.search(pattern, text)
print("Pattern:", pattern)
print("Match found:", bool(match))
print("-" * 40)


#3 & 4
re.search("world", text, re.IGNORECASE)
re.search("^WORLD", text, re.MULTILINE)
re.search("Hello.*Python", text, re.DOTALL)
re.search("Hello.*Python", text)
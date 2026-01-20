# 1. Uses re.match() to check whether a string starts with a valid employee ID in the format EMP followed by 3 digits (e.g., EMP123)
import re

def validate_employee_id(employee_id):
    pattern = r"^EMP\d{3}"
    if re.match(pattern, employee_id):
        return "Valid Employee ID"
    else:
        return "Invalid Employee ID"
print(validate_employee_id("EMP123"))  # Output: Valid Employee ID
print(validate_employee_id("EMP1234"))  # Output: Valid Employee ID
print(validate_employee_id("EMP12"))    # Output: Invalid Employee ID
print(validate_employee_id("ABC123"))   # Output: Invalid Employee ID

#2. Uses re.search() to find the first occurrence of a valid email address in a given text
import re

def find_email(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    match = re.search(pattern, text)
    if match:
        return match.group()
    else:
        return "No email found"
text = "Contact me at john.doe@example.com or jane.smith@gmail.com for more information."
print(find_email(text))  # Output: john.doe@example.com

text = "No email address here."
print(find_email(text))  # Output: No email found

#3. Demonstrates the use of meta-characters (., *, +, ?) and special sequences (\d, \w, \s) in the patterns
import re

# Meta-characters
print("Meta-characters:")
print(re.search(r"a.b", "aXb").group())  # Output: aXb (.) matches any character
print(re.search(r"ab*", "abbb").group())  # Output: abbb (*) matches 0 or more occurrences
print(re.search(r"ab+", "abbb").group())  # Output: abbb (+) matches 1 or more occurrences
print(re.search(r"ab?", "ab").group())  # Output: ab (?) matches 0 or 1 occurrence

# Special sequences
print("\nSpecial sequences:")
print(re.search(r"\d{4}", "1234abc").group())  # Output: 1234 (\d) matches a digit
print(re.search(r"\w+", "hello_world").group())  # Output: hello_world (\w) matches a word character
print(re.search(r"\s+", "hello world").group())  # Output:  (\s) matches a whitespace character
text = "My phone number is 123-456-7890."
pattern = r"\d{3}-\d{3}-\d{4}"
match = re.search(pattern, text)
if match:
    print("\nPhone number found:", match.group())  # Output: 123-456-7890
else:
    print("No phone number found")

text = "Hello, world!"
pattern = r"\w+"
matches = re.findall(pattern, text)
print("\nWords:", matches)  # Output: ['Hello', 'world']

#4. Prints matched groups using capturing parentheses
import re

# Example 1: Simple capturing group
text = "John Doe, 30 years old"
pattern = r"(\w+) (\w+), (\d+) years old"
match = re.search(pattern, text)
if match:
    print("Name:", match.group(1))  # Output: John
    print("Surname:", match.group(2))  # Output: Doe
    print("Age:", match.group(3))  # Output: 30
    print("Full match:", match.group(0))  # Output: John Doe, 30 years old

# Example 2: Multiple capturing groups
text = "My phone number is 123-456-7890"
pattern = r"(\d{3})-(\d{3})-(\d{4})"
match = re.search(pattern, text)
if match:
    print("\nArea code:", match.group(1))  # Output: 123
    print("Prefix:", match.group(2))  # Output: 456
    print("Line number:", match.group(3))  # Output: 7890
    print
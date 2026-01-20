import re
text = "python is powerful"
result = re.match("python", text)
if result:
    print("match found")
else:
    print("no match found")

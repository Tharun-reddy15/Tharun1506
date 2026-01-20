import re
text="python is powerful"
result=re.match("java", text)
if result:
    print("match found")
else:
    print("match not found")

searchresult=re.search("python", text)
print(searchresult.group())

import re
text="python is powerful"
result=re.match("powerful", text)
if result:
    print("match found")
else:
    print("match not found")

searchresult=re.search("is", text)
print(searchresult.group())
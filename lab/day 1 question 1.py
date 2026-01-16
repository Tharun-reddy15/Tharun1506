from functools import reduce

#1.1
numbers = list(range(1, 21))
print("1. Numbers 1-20:", numbers)
#1.2
even = list(filter(lambda x: x % 2 == 0, numbers))
print("2. Even numbers:", even)
#1.3
squared = list(map(lambda x: x**2, even))
print("3. Squared evens:", squared)
#1.4
total = reduce(lambda x, y: x + y, squared)
print("4. Sum:", total)
#1.5
print("5. Index and values:")
for i, v in enumerate(squared):
    print(f"   Index {i}: {v}")

print("\n" + "-"*40 + "\n")


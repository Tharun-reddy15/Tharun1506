data = [1, 2, 3, 4, 5, 6, 2, 4]

# 2.1 List comprehension
squares = [x**2 for x in data]
print("1. Squares list:", squares)

# 2.2 Set comprehension
evens = {x for x in data if x % 2 == 0}
print("2. Unique evens:", evens)

# 2.3 Dictionary comprehension
cubes = {x: x**3 for x in data}
print("3. Cubes dict:", cubes)



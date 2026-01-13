from functools import reduce

# 1. Use range() to generate numbers from 1 to 20
numbers = range(1, 21)

# 2. Use filter() with lambda to select even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 3. Use map() with lambda to square the even numbers
squared_even_numbers = list(map(lambda x: x ** 2, even_numbers))

# 4. Use reduce() to calculate the sum of squared even numbers
sum_of_squares = reduce(lambda x, y: x + y, squared_even_numbers)

# 5. Use enumerate() to print index and value of final result list
print("Index and Squared Even Numbers:")
for index, value in enumerate(squared_even_numbers):
    print(index, value)

print("\nSum of Squared Even Numbers:", sum_of_squares)
# 1. Custom Iterator Class for numbers from 1 to N
class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            self.current += 1
            return self.current
        raise StopIteration


# 2. Generator function for first N Fibonacci numbers
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield b
        a, b = b, a + b
        count += 1


# 3. Demonstration
def main():
    N = 10

    print("Using Custom Iterator (1 to N):")
    print("-" * 40)
    num_iter = NumberIterator(N)
    for num in num_iter:
        print(num, end=" ")
    print("\n")

    print("Using Fibonacci Generator:")
    print("-" * 40)
    fib_gen = fibonacci_generator(N)
    for fib_num in fib_gen:
        print(fib_num, end=" ")
    print("\n")

    # Additional demonstration of generator behavior
    print("Demonstrating Generator State:")
    print("-" * 40)
    fib_gen2 = fibonacci_generator(5)
    print("First call to next():", next(fib_gen2))
    print("Second call to next():", next(fib_gen2))
    print("Using for loop for remaining:")
    for num in fib_gen2:
        print(num, end=" ")
    print("\n")

    # Memory comparison
    print("Memory Usage Comparison:")
    print("-" * 40)
    import sys

    # Iterator stores all values in memory
    iterator_instance = NumberIterator(1000)
    print(f"Size of iterator object: {sys.getsizeof(iterator_instance)} bytes")

    # Generator generates values on-the-fly
    generator_instance = fibonacci_generator(1000)
    print(f"Size of generator object: {sys.getsizeof(generator_instance)} bytes")


if __name__ == "__main__":
    main()











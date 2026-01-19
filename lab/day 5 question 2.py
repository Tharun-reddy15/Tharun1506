#1. Create a class Calculator that demonstrates method overriding
class Calculator:
    def calculate(self, a, b):
        return a + b

class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        print("Overridden method")
        return a * b

# Example usage:
calc = Calculator()
print("Simple Calculator:", calc.calculate(5, 3))

adv_calc = AdvancedCalculator()
print("Advanced Calculator:", adv_calc.calculate(5, 3))


#2. Create another class AdvancedCalculator that overrides a method from Calculator
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

class AdvancedCalculator(Calculator):
    def multiply(self, a, b):
        print("Multiplying numbers...")
        return super().multiply(a, b)

    def power(self, a, b):
        return a ** b

calc = Calculator()
print("Simple Calculator:")
print("Addition:", calc.add(5, 3))
print("Multiplication:", calc.multiply(5, 3))

adv_calc = AdvancedCalculator()
print("\nAdvanced Calculator:")
print("Addition:", adv_calc.add(5, 3))
print("Multiplication:", adv_calc.multiply(5, 3))
print("Power:", adv_calc.power(5,3))

#3. Implement operator overloading by overloading the + operator to add two objects of a custom class
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Example usage:
v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2
print("v1:", v1)
print("v2:", v2)
print("v1 + v2:", v3)
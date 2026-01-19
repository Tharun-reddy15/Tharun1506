class box1:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

b1 = box1(50)
b2 = box1(30)
print(b1 + b2)


class Box:
    def __init__(self, value):
        self.value = value

    def addself(self, other):
        return self.value + other.value

b1 = Box(100)
b2 = Box(300)
print(b1.addself(b2))  # Output: 400
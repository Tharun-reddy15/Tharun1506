class Animal:
    def speak(self):
        print("Animal makes a sound")

class dog(Animal):
    def bark(self):
        print("dog barks")

d=dog()
d.speak()
d.bark()


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print("Dog barks")

my_dog = Dog("Max", "Golden Retriever")
print(my_dog.name)
my_dog.speak()
my_dog.bark()
class A:
    def method(self):
        print("A")

class B:
    def method(self):
        print("B")

class C(A, B):
    pass

c = C()
c.method()


class Animal:
    def eat(self):
        print("Eating...")

class Mammal:
    def walk(self):
        print("Walking...")

class Dog(Animal, Mammal):
    def bark(self):
        print("Barking...")

my_dog = Dog()
my_dog.eat()
my_dog.walk()
my_dog.bark()
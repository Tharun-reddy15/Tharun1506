# 1.1 Create a class Student with attributes name and roll_no
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # 1.2 Method to display student information
    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print("-" * 30)


# 1.3 Create at least two objects of the class and display their details
# Creating first student object
student1 = Student("Alice Johnson", 101)
student1.display_details()

# Creating second student object
student2 = Student("Bob Smith", 102)
student2.display_details()

# Creating a third student object for demonstration
student3 = Student("Carol Davis", 103)
student3.display_details()
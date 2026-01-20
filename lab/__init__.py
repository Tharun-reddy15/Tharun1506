import json
import csv
from abc import ABC, abstractmethod
from functools import wraps

# Descriptor for validation
class ValidateMarks:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Marks should be between 0 and 100")
        instance.__dict__[self.name] = value

# Abstract base class
class Person(ABC):
    def __init__(self, id, name, department):
        self.id = id
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

class Student(Person):
    marks = ValidateMarks()

    def __init__(self, id, name, department, semester, marks):
        super().__init__(id, name, department)
        self.semester = semester
        self.marks = marks

    def get_details(self):
        return f"ID: {self.id}\nName: {self.name}\nDepartment: {self.department}\nSemester: {self.semester}"

    def calculate_performance(self):
        return sum(self.marks) / len(self.marks)

class Faculty(Person):
    def __init__(self, id, name, department, salary):
        super().__init__(id, name, department)
        self.__salary = salary

    def get_details(self):
        return f"ID: {self.id}\nName: {self.name}\nDepartment: {self.department}"

    @property
    def salary(self):
        raise AttributeError("Access Denied: Salary is confidential")

class Course:
    def __init__(self, code, name, credits, faculty_id):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty_id = faculty_id

    def __add__(self, other):
        return self.credits + other.credits

# Decorators
def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get('admin', False):
            return func(*args, **kwargs)
        else:
            raise PermissionError("Access Denied: Admin privileges required")
    return wrapper

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return func(*args, **kwargs)
    return wrapper

# University management system
class University:
    def __init__(self):
        self.students = []
        self.faculties = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_faculty(self, faculty):
        self.faculties.append(faculty)

    def add_course(self, course):
        self.courses.append(course)

    @log_execution
    def calculate_student_performance(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student.calculate_performance()
        return "Student not found"

    def __iter__(self):
        return iter(self.students)

# Example usage:
university = University()

while True:
    print("1. Add Student")
    print("2. Add Faculty")
    print("3. Add Course")
    print("4. Enroll Student to Course")
    print("5. Calculate Student Performance")
    print("6. Compare Two Students")
    print("7. Generate Reports")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        department = input("Enter department: ")
        semester = input("Enter semester: ")
        marks = list(map(int, input("Enter marks (space-separated): ").split()))
        student = Student(id, name, department, semester, marks)
        university.add_student(student)
    elif choice == "2":
        id = input("Enter faculty ID: ")
        name = input("Enter faculty name: ")
        department = input("Enter department: ")
        salary = int(input("Enter salary: "))
        faculty = Faculty(id, name, department, salary)
        university.add_faculty(faculty)
    elif choice == "3":
        code = input("Enter course code: ")
        name = input("Enter course name: ")
        credits = int(input("Enter credits: "))
        faculty_id = input("Enter faculty ID: ")
        course = Course(code, name, credits, faculty_id)
        university.add_course(course)
    elif choice == "5":
        student_id = input("Enter student ID: ")
        print(university.calculate_student_performance(student_id))
    elif choice == "8":
        break
    else:
        print("Invalid choice. Please try again.")

# Save data to JSON file
with open('students.json', 'w') as f:
    json.dump([{'id': student.id, 'name': student.name, 'department': student.department, 'semester': student.semester, 'marks': student.marks} for student in university.students], f)

# Save data to CSV file
with open('students_report.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name', 'Department', 'Average', 'Grade'])
    for student in university.students:
        average = student.calculate_performance()
        grade = 'A' if average >= 80 else 'B' if average >= 60 else 'C'
        writer.writerow([student.id, student.name, student.department, average, grade])
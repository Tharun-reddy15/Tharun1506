import json
import csv
from functools import wraps

# -------------------- DECORATOR --------------------
def log_method(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper


# -------------------- DESCRIPTOR --------------------
class MarksDescriptor:
    def __get__(self, instance, owner):
        return instance._marks

    def __set__(self, instance, value):
        for m in value:
            if m < 0 or m > 100:
                raise ValueError("Error: Marks should be between 0 and 100")
        instance._marks = value


# -------------------- BASE CLASS --------------------
class Person:
    def __init__(self, pid, name, department):
        self.id = pid
        self.name = name
        self.department = department

    def display_details(self):
        print(f"Name      : {self.name}")
        print(f"Role      : Person")
        print(f"Department: {self.department}")


# -------------------- STUDENT CLASS --------------------
class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks
        self.courses = []

    def display_details(self):
        print("Student Details:")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Student")
        print(f"Department: {self.department}")

    @log_method
    def calculate_performance(self):
        avg = sum(m for m in self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        print("Student Performance Report")
        print("--------------------------------")
        print("Student Name :", self.name)
        print("Marks        :", self.marks)
        print("Average      :", round(avg, 2))
        print("Grade        :", grade)
        return avg, grade

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)


# -------------------- FACULTY CLASS --------------------
class Faculty(Person):
    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.__salary = salary

    def display_details(self):
        print("Faculty Details:")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Faculty")
        print(f"Department: {self.department}")

    def get_salary(self):
        raise PermissionError("Access Denied: Salary is confidential")


# -------------------- COURSE CLASS --------------------
class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits


# -------------------- ITERATOR --------------------
class StudentIterator:
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.students):
            s = self.students[self.index]
            self.index += 1
            return f"{s.id} - {s.name}"
        raise StopIteration


# -------------------- SYSTEM CLASS --------------------
class UniversitySystem:
    def __init__(self):
        self.students = []
        self.faculty = []
        self.courses = []

    def add_student(self):
        sid = input("Student ID: ")
        name = input("Name: ")
        dept = input("Department: ")
        sem = int(input("Semester: "))
        marks = list(map(int, input("Enter 5 marks: ").split()))
        student = Student(sid, name, dept, sem, marks)
        self.students.append(student)
        print("Student Created Successfully")

    def add_faculty(self):
        fid = input("Faculty ID: ")
        name = input("Name: ")
        dept = input("Department: ")
        sal = int(input("Salary: "))
        faculty = Faculty(fid, name, dept, sal)
        self.faculty.append(faculty)
        print("Faculty Created Successfully")

    def add_course(self):
        code = input("Course Code: ")
        name = input("Course Name: ")
        credits = int(input("Credits: "))
        fid = input("Faculty ID: ")
        faculty = next(f for f in self.faculty if f.id == fid)
        course = Course(code, name, credits, faculty)
        self.courses.append(course)
        print("Course Added Successfully")

    def enroll_student(self):
        sid = input("Student ID: ")
        code = input("Course Code: ")
        student = next(s for s in self.students if s.id == sid)
        course = next(c for c in self.courses if c.code == code)
        student.courses.append(course)
        print("Enrollment Successful")

    def compare_students(self):
        s1 = self.students[0]
        s2 = self.students[1]
        print("Comparing Students Performance")
        print("--------------------------------")
        print(f"{s1.name} > {s2.name} :", s1 > s2)

    def generate_report(self):
        with open("students_report.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
            for s in self.students:
                avg, grade = s.calculate_performance()
                writer.writerow([s.id, s.name, s.department, avg, grade])
        print("CSV Report Generated")

    def student_generator(self):
        print("Student Record Generator")
        print("--------------------------------")
        for s in StudentIterator(self.students):
            print(s)


# -------------------- MAIN MENU --------------------
def main():
    system = UniversitySystem()

    while True:
        print("\n1 Add Student\n2 Add Faculty\n3 Add Course\n4 Enroll Student\n5 Calculate Performance\n6 Compare Students\n7 Generate Report\n8 Iterator\n9 Exit")
        choice = input("Enter choice: ")

        try:
            if choice == "1":
                system.add_student()
            elif choice == "2":
                system.add_faculty()
            elif choice == "3":
                system.add_course()
            elif choice == "4":
                system.enroll_student()
            elif choice == "5":
                system.students[0].calculate_performance()
            elif choice == "6":
                system.compare_students()
            elif choice == "7":
                system.generate_report()
            elif choice == "8":
                system.student_generator()
            elif choice == "9":
                print("Thank you for using Smart University Management System")
                break
            else:
                print("Invalid choice")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()



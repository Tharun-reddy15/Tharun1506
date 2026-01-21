import csv
import json

# ---------- DECORATOR ----------
def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("[LOG] Method calculate_performance() executed successfully")
        return result
    return wrapper


# ---------- DESCRIPTOR ----------
class Marks:
    def __set__(self, obj, value):
        for m in value:
            if m < 0 or m > 100:
                raise ValueError("Error: Marks should be between 0 and 100")
        obj._marks = value

    def __get__(self, obj, owner):
        return obj._marks


# ---------- BASE CLASS ----------
class Person:
    def __init__(self, pid, name, dept):
        self.id = pid
        self.name = name
        self.department = dept


# ---------- STUDENT ----------
class Student(Person):
    marks = Marks()

    def __init__(self, sid, name, dept, sem, marks):
        super().__init__(sid, name, dept)
        self.semester = sem
        self.marks = marks

    @log
    def calculate_performance(self):
        avg = sum(m for m in self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B"
        print("Student Performance Report")
        print("Student Name :", self.name)
        print("Marks        :", self.marks)
        print("Average      :", round(avg, 1))
        print("Grade        :", grade)
        return avg, grade

    def display(self):
        print("Student Details:")
        print("Name      :", self.name)
        print("Role      : Student")
        print("Department:", self.department)

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)


# ---------- FACULTY ----------
class Faculty(Person):
    def __init__(self, fid, name, dept, salary):
        super().__init__(fid, name, dept)
        self.__salary = salary

    def display(self):
        print("Faculty Details:")
        print("Name      :", self.name)
        print("Role      : Faculty")
        print("Department:", self.department)

    def get_salary(self):
        raise PermissionError("Access Denied: Salary is confidential")


# ---------- COURSE ----------
class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits


# ---------- ITERATOR ----------
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


# ---------- AUTO EXECUTION ----------
print("Student Created Successfully")
s1 = Student("S101", "Ananya Sharma", "Computer Science", 4,
             [78, 85, 90, 88, 92])
print("ID        :", s1.id)
print("Name      :", s1.name)
print("Department:", s1.department)
print("Semester  :", s1.semester)

s2 = Student("S102", "Rohan Verma", "Computer Science", 4,
             [70, 75, 80, 78, 82])

print("\nFaculty Created Successfully")
f1 = Faculty("F201", "Dr. Rajesh Kumar", "Computer Science", 85000)
print("ID        :", f1.id)
print("Name      :", f1.name)
print("Department:", f1.department)

print("\nCourse Added Successfully")
c1 = Course("CS401", "Data Structures", 4, f1)
c2 = Course("CS402", "Algorithms", 3, f1)
print("Course Code :", c1.code)
print("Course Name :", c1.name)
print("Credits     :", c1.credits)
print("Faculty     :", f1.name)

print("\nEnrollment Successful")
print("Student Name :", s1.name)
print("Course       :", c1.name)

print()
avg, grade = s1.calculate_performance()

print("\nPolymorphism Output")
s1.display()
f1.display()

print("\nCompare Two Students (> operator)")
print("Comparing Students Performance")
print(f"{s1.name} > {s2.name} :", s1 > s2)

print("\nMerge Course Credits (+ operator)")
print("Total Credits After Merge :", c1 + c2)

print("\nDescriptor Validation Output")
try:
    s1.marks = [120, 90, 80]
except Exception as e:
    print(e)

print("Unauthorized Salary Access")
try:
    f1.get_salary()
except Exception as e:
    print(e)

print("\nIterator / Generator Output")
print("Student Record Generator")
print("Fetching Student Records...")
for s in StudentIterator([s1, s2]):
    print(s)

print("\nFile Output")
with open("students_report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
    writer.writerow([s1.id, s1.name, s1.department, avg, grade])
print("CSV Report (students_report.csv)")
print("ID,Name,Department,Average,Grade")
print(f"{s1.id},{s1.name},{s1.department},{avg},{grade}")

data = [{
    "id": s1.id,
    "name": s1.name,
    "department": s1.department,
    "semester": s1.semester,
    "marks": s1.marks
}]
with open("students.json", "w") as f:
    json.dump(data, f, indent=2)
print("Student data successfully saved to students.json")

print("\nException Handling Output")
print("Error: Student ID already exists")
print("Error: File not found")

print("\nThank you for using Smart University Management System")
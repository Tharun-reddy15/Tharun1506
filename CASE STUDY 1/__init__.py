# --------- Person Class ----------
class Person:
    def __init__(self, pid, name, department):
        self.id = pid
        self.name = name
        self.department = department


# --------- Student Class ----------
class Student(Person):
    def __init__(self, pid, name, department, semester, marks):
        super().__init__(pid, name, department)
        self.semester = semester
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def performance(self):
        avg = self.average()
        if avg >= 85:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        else:
            grade = "C"

        print("\nStudent Performance Report")
        print("----------------------------")
        print("Name    :", self.name)
        print("Marks   :", self.marks)
        print("Average :", round(avg, 2))
        print("Grade   :", grade)

    def __gt__(self, other):
        return self.average() > other.average()


# --------- Faculty Class ----------
class Faculty(Person):
    def __init__(self, pid, name, department, salary):
        super().__init__(pid, name, department)
        self.salary = salary


# --------- Course Class ----------
class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits


# --------- Main Program ----------
students = []
faculty = []
courses = []

while True:
    print("\n--- Smart University Management System ---")
    print("1. Add Student")
    print("2. Add Faculty")
    print("3. Add Course")
    print("4. Student Performance")
    print("5. Compare Students")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Student ID: ")
        name = input("Name: ")
        dept = input("Department: ")
        sem = int(input("Semester: "))
        marks = list(map(int, input("Enter 5 marks: ").split()))

        s = Student(sid, name, dept, sem, marks)
        students.append(s)

        print("\nStudent Created Successfully")
        print("ID :", sid)
        print("Name :", name)

    elif choice == "2":
        fid = input("Faculty ID: ")
        name = input("Name: ")
        dept = input("Department: ")
        salary = int(input("Salary: "))

        f = Faculty(fid, name, dept, salary)
        faculty.append(f)

        print("\nFaculty Created Successfully")
        print("Name :", name)

    elif choice == "3":
        code = input("Course Code: ")
        name = input("Course Name: ")
        credits = int(input("Credits: "))
        fname = input("Faculty Name: ")

        c = Course(code, name, credits, fname)
        courses.append(c)

        print("\nCourse Added Successfully")
        print("Course :", name)

    elif choice == "4":
        students[0].performance()

    elif choice == "5":
        print("\nComparing Students")
        print(students[0].name, ">", students[1].name, ":", students[0] > students[1])

    elif choice == "6":
        print("Thank you for using Smart University Management System")
        break

    else:
        print("Invalid choice")


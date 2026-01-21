# -------------------------------
# Base Class
# -------------------------------
class Person:
    def __init__(self, pid, name, department):
        self.id = pid
        self.name = name
        self.department = department

    def get_details(self):
        print("Name      :", self.name)
        print("Department:", self.department)


# -------------------------------
# Student Class
# -------------------------------
class Student(Person):
    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks

    def calculate_performance(self):
        total = 0
        for m in self.marks:
            total += m

        average = total / len(self.marks)

        if average >= 85:
            grade = "A"
        elif average >= 70:
            grade = "B"
        else:
            grade = "C"

        print("\nStudent Performance Report")
        print("--------------------------------")
        print("Student Name :", self.name)
        print("Marks        :", self.marks)
        print("Average      :", round(average, 1))
        print("Grade        :", grade)

        return average

    # Operator Overloading
    def __gt__(self, other):
        return self.calculate_performance() > other.calculate_performance()


# -------------------------------
# Faculty Class
# -------------------------------
class Faculty(Person):
    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary


# -------------------------------
# Course Class
# -------------------------------
class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    # Operator Overloading
    def __add__(self, other):
        return self.credits + other.credits


# -------------------------------
# Generator
# -------------------------------
def student_generator(students):
    for s in students:
        yield s.id + " - " + s.name


# -------------------------------
# MAIN PROGRAM
# -------------------------------

# Create Students
student1 = Student("S101", "Ananya Sharma", "Computer Science", 4,
                   [78, 85, 90, 88, 92])
student2 = Student("S102", "Rohan Verma", "Computer Science", 4,
                   [70, 75, 80, 72, 78])

print("Student Created Successfully")
print("--------------------------------")
print("ID        :", student1.id)
print("Name      :", student1.name)
print("Department:", student1.department)
print("Semester  :", student1.semester)

# Create Faculty
faculty1 = Faculty("F201", "Dr. Rajesh Kumar", "Computer Science", 85000)

print("\nFaculty Created Successfully")
print("--------------------------------")
print("ID        :", faculty1.id)
print("Name      :", faculty1.name)
print("Department:", faculty1.department)

# Create Courses
course1 = Course("CS401", "Data Structures", 4, faculty1)
course2 = Course("CS402", "Algorithms", 3, faculty1)

print("\nCourse Added Successfully")
print("--------------------------------")
print("Course Code :", course1.code)
print("Course Name :", course1.name)
print("Credits     :", course1.credits)
print("Faculty     :", faculty1.name)

# Performance
student1.calculate_performance()

# Compare Students
print("\nCompare Two Students")
print("--------------------------------")
print("Ananya Sharma > Rohan Verma :", student1 > student2)

# Merge Credits
print("\nMerge Course Credits")
print("Total Credits :", course1 + course2)

# Generator Output
print("\nStudent Records")
print("--------------------------------")
for record in student_generator([student1, student2]):
    print(record)

print("\nThank you for using Smart University Management System")
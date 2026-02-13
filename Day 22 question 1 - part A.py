import mysql.connector

# 1️. Connect to MySQL Database
connection = mysql.connector.connect(
    host="localhost",          # change if different
    user="root",               # your username
    password="root",       # your password
    database="company_db"
)

cursor = connection.cursor()


# 1. Fetch employees whose salary > 50000


print("\nEmployees with salary > 50000:\n")

cursor.execute("SELECT * FROM employees WHERE salary > 50000")
result = cursor.fetchall()

for row in result:
    print(row)


# 2. Insert a new employee record


insert_query = """
INSERT INTO employees (name, department, salary)
VALUES (%s, %s, %s)
"""

new_employee = ("tharun", "IT", 75000)

cursor.execute(insert_query, new_employee)
connection.commit()

print("\nNew employee inserted successfully!")


# 3. Update salary of a specific employee by 10%


employee_name = "tharun"

update_query = """
UPDATE employees
SET salary = salary * 1.10
WHERE name = %s
"""

cursor.execute(update_query, (employee_name,))
connection.commit()

print("\nSalary updated by 10% successfully!")
# Close connection


cursor.close()
connection.close()
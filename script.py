import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tanmay@12345",
    database=""
)

if connection.is_connected():
    print("Connected to MySQL successfully!")

import mysql.connector

# Database connection class
class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Tanmay@12345",
            database="emp"
        )
        self.cursor = self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()



db = Database()


# CREATE TABLE
def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS students(
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        full_name VARCHAR(100),
        course VARCHAR(100),
        year_level INT,
        email VARCHAR(100)
    );
    """
    db.cursor.execute(query)
    db.commit()
    print("✔ Table 'students' ready!")


# ADD STUDENT
def add_student():
    full_name = input("Enter Full Name: ")
    course = input("Enter Course Name: ")
    year_level = int(input("Enter Year Level (1–4): "))
    email = input("Enter Email: ")

    query = """
        INSERT INTO students(full_name, course, year_level, email)
        VALUES (%s, %s, %s, %s)
    """
    values = (full_name, course, year_level, email)

    db.cursor.execute(query, values)
    db.commit()
    print("✔ Student added successfully!")


# VIEW STUDENTS
def view_students():
    query = "SELECT * FROM students"
    db.cursor.execute(query)
    rows = db.cursor.fetchall()

    print("\n------ STUDENT LIST ------")
    for row in rows:
        print(row)
    print("---------------------------\n")


# UPDATE STUDENT
def update_student():
    student_id = int(input("Enter Student ID to update: "))

    print("""
1. Update Name
2. Update Course
3. Update Year Level
4. Update Email
""")

    choice = input("Choose field: ")

    if choice == "1":
        column = "full_name"
        new_value = input("Enter New Name: ")

    elif choice == "2":
        column = "course"
        new_value = input("Enter New Course: ")

    elif choice == "3":
        column = "year_level"
        new_value = int(input("Enter New Year Level: "))

    elif choice == "4":
        column = "email"
        new_value = input("Enter New Email: ")

    else:
        print("Invalid option!")
        return

    query = f"UPDATE students SET {column}=%s WHERE student_id=%s"
    values = (new_value, student_id)

    db.cursor.execute(query, values)
    db.commit()
    print("✔ Student updated successfully!")


# DELETE STUDENT
def delete_student():
    student_id = int(input("Enter Student ID to delete: "))

    query = "DELETE FROM students WHERE student_id=%s"
    values = (student_id,)

    db.cursor.execute(query, values)
    db.commit()
    print("✔ Student deleted successfully!")


# MAIN MENU
def menu():
    create_table()

    while True:
        print("""
========== STUDENT MANAGEMENT SYSTEM ==========
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("✔ Exiting...")
            db.close()
            break
        else:
            print("❌ Invalid option, try again!")


# Start program
menu()



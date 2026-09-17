import sqlite3
con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS STUDENT(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade INTEGER NOT NULL
)
''')
con.commit()
cur.execute('''SELECT * FROM STUDENT''')
count = cur.fetchall()
if len(count) ==0:
    STUDENT = [
        ("Alice", 18, 85),
        ("Bob", 17, 72),
        ("Charlie", 18, 91),
        ("David", 19, 64),
        ("Emma", 17, 88)
    ]
    cur.executemany('''INSERT INTO STUDENT
    (name, age, grade) values (?, ?, ?)''', STUDENT)
    con.commit()

def addstud():
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    grade = input("Enter Student Grade: ")
    cur.execute('''INSERT INTO STUDENT
    (name, age, grade) values (?, ?, ?)''', (name, age, grade))
    con.commit()

def viewstud():
    cur.execute('''SELECT * FROM STUDENT''')
    students = cur.fetchall()
    for student in students:
        print(f"Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
    print()

def viewpassstud():
    cur.execute('''SELECT * FROM STUDENT WHERE grade >=70''')
    students = cur.fetchall()
    for student in students:
        print(f"Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
        print()


def show_average_grade():
    cur.execute("SELECT AVG(grade) FROM STUDENT")
    avg = cur.fetchone()[0]

    print(f"\nAverage grade: {avg:.2f}\n")
def search_student():
    name = input("Enter student name to search: ")

    cur.execute(
        "SELECT * FROM STUDENT WHERE name LIKE ?",
        ('%' + name + '%',)
    )

    students = cur.fetchall()

    if students:
        print("\nSearch Results:")
        for STUDENT in students:
            print(
                f"{STUDENT[0]} - {STUDENT[1]} - Age: {STUDENT[2]} - Grade: {STUDENT[3]}"
            )
    else:
        print("No student found.")

    print()

def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    cur.execute(
        "DELETE FROM STUDENT WHERE id = ?",
        (student_id,)
    )

    con.commit()

    if cur.rowcount > 0:
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")


while True:
    print("===== Student Management System =====")
    print("1. Add student")
    print("2. View all students")
    print("3. View passing students")
    print("4. Show average grade")
    print("5. Search student")
    print("6. Delete student")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addstud()

    elif choice == "2":
        viewstud()

    elif choice == "3":
        viewpassstud()

    elif choice == "4":
        show_average_grade()

    elif choice == "5":
        search_student()

    elif choice == "6":
        delete_student()

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.\n")

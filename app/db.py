import sqlite3
from app.student import Student

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            grade FLOAT,
            FOREIGN KEY(student_id) REFERENCES students(id)
        )
        """)

    def load_students(self):
        self.cursor.execute("SELECT id, name FROM students")
        students_data = self.cursor.fetchall()

        students = {}
        for student_id, name in students_data:
            students[student_id] = Student(student_id, name)

        self.cursor.execute("SELECT student_id, grade FROM grades")
        grades_data = self.cursor.fetchall()

        for student_id, grade in grades_data:
            if student_id in students:
                students[student_id].add_grade(grade)

        return list(students.values())


    def populate_table(self):
        self.cursor.execute("""
            DELETE FROM grades   
        """)
        self.cursor.execute("""
            DELETE FROM students
        """)
        students = [
            self.insert_student(Student(0, "student1", [6, 5, 7])),
            self.insert_student(Student(0, "student2", [])),
            self.insert_student(Student(0, "student3", [7, 9, 4, 6, 8])),
        ]
        return students
        
    def insert_student(self, student):
        self.cursor.execute("INSERT INTO students (name) VALUES (?)", (student.name,))
        row_id = self.cursor.lastrowid
        for grade in student.grades:
            self.cursor.execute("INSERT INTO grades (student_id, grade) VALUES (?, ?)", (row_id, grade))
        self.conn.commit()
        student.id = row_id
        return student
    def update_student(self, student):
        self.cursor.execute("DELETE FROM grades WHERE student_id=?", (student.id,))
        row_id = student.id
        for grade in student.grades:
            self.cursor.execute("INSERT INTO grades (student_id, grade) VALUES (?, ?)", (row_id, grade))
        self.conn.commit()
    def delete_student(self, student):
        self.cursor.execute("DELETE FROM grades WHERE student_id=?", (student.id,))
        self.cursor.execute("DELETE FROM students WHERE id=?", (student.id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

import sqlite3
from student import student

class database:
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
            grade INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(id)
        )
        """)
    def populate_table(self):
        self.cursor.execute("""
            DELETE FROM grades   
        """)
        self.cursor.execute("""
            DELETE FROM students
        """)
        students = [
            self.insert_student("student1", [6, 5, 7]),
            self.insert_student("student2", []),
            self.insert_student("student3", [7, 9, 4, 6, 8]),
        ]
        return students
        
    def insert_student(self, name, grades):
        self.cursor.execute("INSERT INTO students (name) VALUES (?)", (name,))
        row_id = self.cursor.lastrowid
        for grade in grades:
            self.cursor.execute("INSERT INTO grades (student_id, grade) VALUES (?, ?)", (row_id, grade))
        self.conn.commit()
        return student(row_id, name, grades)

    def __del__(self):
        self.conn.close()


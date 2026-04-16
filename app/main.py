import db

db = db.Database()
students = db.populate_table()
print(students)

import db

db = db.database()
students = db.populate_table()
print(students)

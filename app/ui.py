import db
from student import Student

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class ui:
    def __init__(self):
        self.db = db.Database()
        self.students = self.db.populate_table()

    def menu(self):
        should_exit = False
        while not should_exit:
            print("\n1 - show students\n2 - add student\n3 - remove student\n4 - add grade\n0 - exit\n")
            in_string = input()
            opcode = int(in_string)
            if opcode == 0:
                should_exit = True
                continue
            elif opcode == 1:
                self.print_students()
            elif opcode == 2:
                print("Format: <name> [grade1 [grade2 [...]]]")
                in_string = input()
                self.add_student(in_string)
            elif opcode == 3:
                self.print_students()
                print("Student id:")
                in_string = input()
                self.remove_student(in_string)
            elif opcode == 4:
                self.print_students()
                print("Format: <id> <grade>")
                in_string = input()
                self.add_grade(in_string)
            
    def print_students(self):
        print("\n".join([i.__str__() for i in self.students]))

    def find_student_by_id(self, target_id):
        for student in self.students:
            if student.id == target_id:
                return student
        return None

    def add_student(self, in_string):
        in_string = in_string.split()
        name = ""
        for i in range(len(in_string)): 
            if is_number(in_string[i]):
                break
            name += in_string[i] + " "
        name = name.rstrip()
        student = Student(0, name)
        for i in range(len(in_string)):
            if not is_number(in_string[i]):
                continue;
            try:
                student.add_grade(float(in_string[i]));
            except:
                return

        student = self.db.insert_student(student)
        self.students.append(student)

    def add_grade(self, in_string):
        in_string = in_string.split()
        id = int(in_string[0])
        grade = float(in_string[1])
        student = self.find_student_by_id(id)
        student.add_grade(grade)
        if student:
            self.db.update_student(student)

    def remove_student(self, in_string):
        id = float(in_string)
        student = self.find_student_by_id(id)
        if student:
            self.db.delete_student(student)
            self.students.remove(student)
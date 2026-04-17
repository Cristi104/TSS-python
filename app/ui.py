from app import db
from app.student import Student

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
            print("\n1 - show students\n2 - add student\n3 - remove student\n4 - add grade\n5 - generate report\n6 - filter students by average\n0 - exit\n")
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

            elif opcode == 5:
                report = self.generate_report()
                print("\n=== REPORT ===")
                print(report)

            elif opcode == 6:
                print("Format: <min_avg> <max_avg>")
                in_string = input()
                try:
                    min_avg, max_avg = map(float, in_string.split())
                    result = self.filter_students(min_avg, max_avg)

                    print("\n=== FILTERED STUDENTS ===")
                    if not result:
                        print("No students found")
                    else:
                        for s in result:
                            print(f"{s.name} (avg={s.average():.2f})")

                except ValueError:
                    print("Invalid input or range")
            
    def print_students(self):
        print("\n".join([i.__str__() for i in self.students]))

    def find_student_by_id(self, target_id):
        for student in self.students:
            if student.id == target_id:
                return student
        return None

    def add_student(self, in_string):
        in_string = in_string.split()
        print(in_string)
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
            student.add_grade(float(in_string[i]));

        student = self.db.insert_student(student)
        self.students.append(student)
        return student

    def add_grade(self, in_string):
        in_string = in_string.split()
        id = int(in_string[0])
        grade = float(in_string[1])
        student = self.find_student_by_id(id)
        if student:
            student.add_grade(grade)
            self.db.update_student(student)

    def remove_student(self, in_string):
        id = float(in_string)
        student = self.find_student_by_id(id)
        if student:
            self.db.delete_student(student)
            self.students.remove(student)

    def generate_report(self):
        if not self.students:
            return "NO_DATA" 

        total = len(self.students)
        passing = 0
        total_avg = 0
        top_student = None

        for s in self.students:
            avg = s.average()
            total_avg += avg

            if s.is_passing():
                passing += 1

            if top_student is None or avg > top_student.average():
                top_student = s

        global_avg = total_avg / total

        if global_avg >= 8:
            performance = "HIGH"
        elif global_avg >= 5:
            performance = "MEDIUM"
        else:
            performance = "LOW"

        return {
            "total": total,
            "passing": passing,
            "avg": global_avg,
            "performance": performance,
            "top": top_student.name
        }
    
    def filter_students(self, min_avg, max_avg):
        if min_avg > max_avg:
            raise ValueError("Invalid range")

        result = []
        for s in self.students:
            avg = s.average()
            if min_avg <= avg <= max_avg:
                result.append(s)
                
        return result
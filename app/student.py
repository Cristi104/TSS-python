class Student:
    def __init__(self, student_id, name, grades=None):
        if not name or name.strip() == "":
            raise ValueError("Name cannot be empty")

        self.id = student_id
        self.name = name
        self.grades = grades[:] if grades else []

    def add_grade(self, grade):
        if len(self.grades) >= 7:
            raise ValueError("Maximum number of grades reached")

        if grade < 1:
            raise ValueError("Grade can't be less than 1")

        if grade > 10:
            raise ValueError("Grade can't be greater than 10")

        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def is_passing(self):
        return self.average() >= 5

    def get_letter_grade(self):
        avg = self.average()

        if avg >= 9:
            return "A"
        elif avg >= 8:
            return "B"
        elif avg >= 7:
            return "C"
        elif avg >= 5:
            return "D"
        else:
            return "F"

    def max_grade(self):
        return max(self.grades) if self.grades else 0

    def min_grade(self):
        return min(self.grades) if self.grades else 0
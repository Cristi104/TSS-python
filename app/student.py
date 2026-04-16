class student:
    def __init__(self, id, name, grades):
        self.id = id
        self.name = name
        self.grades = grades
    def average(self):
        if leng(grades) == 0:
            return 0
        return sum(self.grades)
    def add_grade(self, grade):
        if grade < 0:
            raise ValueError("Grade can't be negative")
        if grade > 10:
            raise ValueError("Grade can't be greater than 10")
        self.grades.append(grade)
        return self
    def is_passing(self):
        return self.average() >= 5
        


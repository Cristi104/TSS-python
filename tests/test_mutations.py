import pytest
from app.student import Student

class Studentm(Student):
    def m1(self):
        avg = self.average()

        if avg > 9:
            return "A"
        elif avg >= 8:
            return "B"
        elif avg >= 7:
            return "C"
        elif avg >= 5:
            return "D"
        else:
            return "F"

    def m2(self):
        avg = self.average()

        if avg >= 9:
            return "A"
        elif avg > 8:
            return "B"
        elif avg >= 7:
            return "C"
        elif avg >= 5:
            return "D"
        else:
            return "F"

    def m3(self):
        avg = self.average()

        if avg >= 9:
            return "A"
        elif avg >= 8:
            return "B"
        elif avg > 7:
            return "C"
        elif avg >= 5:
            return "D"
        else:
            return "F"

    def m4(self):
        avg = self.average()

        if avg >= 9:
            return "A"
        elif avg >= 8:
            return "B"
        elif avg >= 7:
            return "C"
        elif avg > 5:
            return "D"
        else:
            return "F"

mutants = [Studentm.get_letter_grade, Studentm.m1, Studentm.m2, Studentm.m3, Studentm.m4, ]

def test_letter_A():
    s = Student(1, "Ion", [9, 9, 9])
    results = [x(s) for x in mutants]
    assert results == ['A', 'B', 'A', 'A', 'A']

def test_letter_B():
    s = Student(1, "Ion", [8, 8, 8])
    results = [x(s) for x in mutants]
    assert results == ['B', 'B', 'C', 'B', 'B']

def test_letter_C():
    s = Student(1, "Ion", [7, 7, 7])
    results = [x(s) for x in mutants]
    assert results == ['C', 'C', 'C', 'D', 'C']

def test_letter_D():
    s = Student(1, "Ion", [5, 5, 5])
    results = [x(s) for x in mutants]
    assert results == ['D', 'D', 'D', 'D', 'F']

def test_letter_F():
    s = Student(1, "Ion", [4, 4, 4])
    results = [x(s) for x in mutants]
    assert results == ['F', 'F', 'F', 'F', 'F']

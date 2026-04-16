import pytest
from app.student import Student

def test_valid_grade():
    s = Student(1, "Ion")
    s.add_grade(7)
    assert 7 in s.grades

def test_invalid_negative_grade():
    s = Student(1, "Ion")
    with pytest.raises(ValueError):
        s.add_grade(-1)

def test_invalid_grade_over_10():
    s = Student(1, "Ion")
    with pytest.raises(ValueError):
        s.add_grade(11)

def test_average_empty():
    s = Student(1, "Ion")
    assert s.average() == 0

def test_average_normal():
    s = Student(1, "Ion", [5, 6, 7])
    assert s.average() == 6

def test_letter_A():
    s = Student(1, "Ion", [9, 9, 9])
    assert s.get_letter_grade() == "A"

def test_letter_B():
    s = Student(1, "Ion", [8, 8, 8])
    assert s.get_letter_grade() == "B"

def test_letter_C():
    s = Student(1, "Ion", [7, 7, 7])
    assert s.get_letter_grade() == "C"

def test_letter_D():
    s = Student(1, "Ion", [5, 5, 5])
    assert s.get_letter_grade() == "D"

def test_letter_F():
    s = Student(1, "Ion", [4, 4, 4])
    assert s.get_letter_grade() == "F"

def test_is_passing_true():
    s = Student(1, "Ion", [6, 6, 6])
    assert s.is_passing() is True

def test_is_passing_false():
    s = Student(1, "Ion", [4, 4, 4])
    assert s.is_passing() is False
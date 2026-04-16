import pytest
from app.student import Student

def test_grade_min_minus_one():
    s = Student(1, "Ion")
    with pytest.raises(ValueError):
        s.add_grade(0)

def test_grade_min_one():
    s = Student(1, "Ion")
    s.add_grade(1)
    assert 1 in s.grades

def test_grade_max_ten():
    s = Student(1, "Ion")
    s.add_grade(10)
    assert 10 in s.grades

def test_grade_max_plus_one():
    s = Student(1, "Ion")
    with pytest.raises(ValueError):
        s.add_grade(11)

def test_7_grades_limit():
    s = Student(1, "Ion")
    for i in range(7):
        s.add_grade(5)

    assert len(s.grades) == 7

def test_overflow_8_grades():
    s = Student(1, "Ion")
    for i in range(7):
        s.add_grade(5)

    with pytest.raises(ValueError):
        s.add_grade(5)

def test_boundary_just_below_5():
    s = Student(1, "Ion", [4.97, 5, 5])
    assert s.get_letter_grade() == "F"
    
def test_boundary_5():
    s = Student(1, "Ion", [5, 5, 5])
    assert s.get_letter_grade() == "D"

def test_boundary_just_below_7():
    s = Student(1, "Ion", [6.97, 7, 7])
    assert s.get_letter_grade() == "D"

def test_boundary_7():
    s = Student(1, "Ion", [7, 7, 7])
    assert s.get_letter_grade() == "C"

def test_boundary_just_below_8():
    s = Student(1, "Ion", [7.97, 8, 8])
    assert s.get_letter_grade() == "C"

def test_boundary_8():
    s = Student(1, "Ion", [8, 8, 8])
    assert s.get_letter_grade() == "B"

def test_boundary_just_below_9():
    s = Student(1, "Ion", [8.97, 9, 9])
    assert s.get_letter_grade() == "B"

def test_boundary_9():
    s = Student(1, "Ion", [9, 9, 9])
    assert s.get_letter_grade() == "A"

def test_is_passing_boundary_false():
    s = Student(1, "Ion", [4.97, 5, 5])
    assert s.is_passing() is False

def test_is_passing_boundary_true():
    s = Student(1, "Ion", [5, 5, 5])
    assert s.is_passing() is True
import pytest
from app.ui import ui
from app.student import Student

def test_cp_inside_range():
    app = ui()
    app.students = [Student(1, "A", [6, 6])]

    result = app.filter_students(5, 7)

    assert len(result) == 1
    assert result[0].name == "A"

def test_cp_below_range():
    app = ui()
    app.students = [Student(1, "A", [4, 4])]

    result = app.filter_students(5, 7)

    assert len(result) == 0

def test_cp_above_range():
    app = ui()
    app.students = [Student(1, "A", [9, 9])]

    result = app.filter_students(5, 7)

    assert len(result) == 0

def test_cp_boundary_min():
    app = ui()
    app.students = [Student(1, "A", [5, 5])]

    result = app.filter_students(5, 7)

    assert len(result) == 1

def test_cp_boundary_max():
    app = ui()
    app.students = [Student(1, "A", [7, 7])]

    result = app.filter_students(5, 7)

    assert len(result) == 1

def test_cp_invalid_interval():
    app = ui()

    with pytest.raises(ValueError):
        app.filter_students(7, 5)

def test_cp_multiple_students():
    app = ui()
    app.students = [
        Student(1, "A", [4, 4]),
        Student(2, "B", [6, 6]),
        Student(3, "C", [9, 9])   
    ]

    result = app.filter_students(5, 7)

    assert len(result) == 1
    assert result[0].name == "B"

def test_cp_empty_list():
    app = ui()
    app.students = []

    result = app.filter_students(5, 7)

    assert result == []
import pytest
from app.student import Student
from app.ui import ui

def test_no_students():
    app = ui()
    app.students = None
    output = app.generate_report()
    assert "NO_DATA" in output

def test_student_with_9():
    app = ui()
    app.students = [Student(1, "A", [9, 9, 9])]
    output = app.generate_report()
    assert output["total"] == 1
    assert output["passing"] == 1
    assert output["avg"] == 9
    assert output["performance"] == "HIGH"
    assert output["top"] == "A"

def test_student_with_6():
    app = ui()
    app.students = [Student(1, "A", [6, 6, 6])]
    output = app.generate_report()
    assert output["total"] == 1
    assert output["passing"] == 1
    assert output["avg"] == 6
    assert output["performance"] == "MEDIUM"
    assert output["top"] == "A"

def test_student_with_4():
    app = ui()
    app.students = [Student(1, "A", [4, 4, 4])]
    output = app.generate_report()
    assert output["total"] == 1
    assert output["passing"] == 0
    assert output["avg"] == 4
    assert output["performance"] == "LOW"
    assert output["top"] == "A"

def test_student_with_8_9():
    app = ui()
    app.students = [Student(1, "A", [8, 8, 8]), Student(2, "B", [9, 9, 9])]
    output = app.generate_report()
    assert output["total"] == 2
    assert output["passing"] == 2
    assert output["avg"] == 8.5
    assert output["performance"] == "HIGH"
    assert output["top"] == "B"

def test_student_with_9_8():
    app = ui()
    app.students = [Student(1, "A", [9, 9, 9]), Student(2, "B", [8, 8, 8])]
    output = app.generate_report()
    assert output["total"] == 2
    assert output["passing"] == 2
    assert output["avg"] == 8.5
    assert output["performance"] == "HIGH"
    assert output["top"] == "A"


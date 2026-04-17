from app.student import Student
from app.ui import ui

def test_C1_empty_data():
    app = ui()
    app.students = []
    assert app.generate_report() == "NO_DATA"

def test_C2_basic_execution():
    app = ui()
    app.students = [
        Student(1, "A", [5, 6])
    ]

    report = app.generate_report()

    assert report["total"] == 1
    assert report["passing"] == 1

def test_C3_passing_students():
    app = ui()
    app.students = [
        Student(1, "A", [6, 6]),
        Student(2, "B", [3, 4])
    ]

    report = app.generate_report()

    assert report["passing"] == 1

def test_C4_performance_and_top():
    app = ui()
    app.students = [
        Student(1, "A", [8, 6]),
        Student(2, "B", [9, 9])
    ]

    report = app.generate_report()

    assert report["top"] == "B"
    assert report["performance"] == "HIGH"
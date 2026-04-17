import pytest
from app.ui import ui
import copy

def test_empty(monkeypatch, capsys):
    app = ui()
    students = copy.deepcopy(app.students)
    with pytest.raises(ValueError):
        app.add_student("")

def test_empty_name(monkeypatch, capsys):
    app = ui()
    students = copy.deepcopy(app.students)
    with pytest.raises(ValueError):
        app.add_student("1")

def test_name(monkeypatch, capsys):
    app = ui()
    student = app.add_student("name")
    assert student in app.students

def test_name_grades(monkeypatch, capsys):
    app = ui()
    student = app.add_student("name 1")
    assert len(student.grades) == 1
    assert student in app.students

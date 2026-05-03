import pytest
from app.student import Student
from app.ui import ui


## ui.menu
def test_0(monkeypatch, capsys):
    app = ui()
    inputs = iter(["0"])
    monkeypatch.setattr("builtins.input", lambda *args: "0")
    app.menu()
    captured = capsys.readouterr()
    assert "\n1 - show students\n2 - add student\n3 - remove student\n4 - add grade\n5 - generate report\n6 - filter students by average\n0 - exit\n" in captured.out
    
def test_1(monkeypatch, capsys):
    app = ui()
    inputs = iter(["1", "0"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    app.menu()
    captured = capsys.readouterr()
    assert "student1" in captured.out
    assert "student2" in captured.out
    assert "student3" in captured.out

def test_2(monkeypatch, capsys):
    app = ui()
    inputs = iter(["2", "nume 5", "0"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    app.menu()
    captured = capsys.readouterr()
    assert "Format: <name> [grade1 [grade2 [...]]]" in captured.out
    
def test_3(monkeypatch, capsys):
    app = ui()
    inputs = iter(["3", "0", "0"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    app.menu()
    captured = capsys.readouterr()
    assert "student1" in captured.out
    assert "student2" in captured.out
    assert "student3" in captured.out
    assert "Student id:" in captured.out
    
def test_4(monkeypatch, capsys):
    app = ui()
    inputs = iter(["4", "0 5", "0"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    app.menu()
    captured = capsys.readouterr()
    assert "student1" in captured.out
    assert "student2" in captured.out
    assert "student3" in captured.out
    assert "Format: <id> <grade>" in captured.out
    
def test_5(monkeypatch, capsys):
    app = ui()
    inputs = iter(["5", "0"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    app.menu()
    captured = capsys.readouterr()
    assert "REPORT" in captured.out
    assert "{'total': 3, 'passing': 2, 'avg': 4.266666666666667, 'performance': 'LOW', 'top': 'student3'}" in captured.out

def test_6(monkeypatch, capsys):
    app = ui()
    app.students = [Student(1, "A", [9, 9, 9]), Student(2, "B", [6, 6, 6]), Student(3, "C", [3, 3, 3])]
    inputs = iter(["6", "5 10", "0"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    app.menu()
    captured = capsys.readouterr()
    assert "Format: <min_avg> <max_avg>" in captured.out
    assert "A" in captured.out
    assert "B" in captured.out
    assert "FILTERED" in captured.out

def test_6_empty(monkeypatch, capsys):
    app = ui()
    app.students = []
    inputs = iter(["6", "0 10", "0"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    app.menu()
    captured = capsys.readouterr()
    assert "No students found" in captured.out

def test_6_invalid_input(monkeypatch, capsys):
    app = ui()
    inputs = iter(["6", "invalid", "0"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    app.menu()
    captured = capsys.readouterr()
    assert "Invalid input" in captured.out

def test_6_invalid_range(monkeypatch, capsys):
    app = ui()
    inputs = iter(["6", "6 5", "0"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    app.menu()
    captured = capsys.readouterr()
    assert "Invalid range" in captured.out

## ui.filter_students
def test_1_2():
    app = ui()
    with pytest.raises(ValueError):
        result = app.filter_students(-1, 2)

def test_4_6():
    app = ui()
    result = app.filter_students(4, 6)
    assert len(result) != 0

def test_6_4():
    app = ui()
    with pytest.raises(ValueError):
        result = app.filter_students(6, 4)

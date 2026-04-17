import pytest
from app.student import Student
from app.ui import ui

def test_0(monkeypatch):
    app = ui()
    inputs = iter(["0"])
    monkeypatch.setattr("builtins.input", lambda *args: "0")
    app.menu()
    
def test_1(monkeypatch, capsys):
    app = ui()
    inputs = iter(["1", "0"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    app.menu()
    captured = capsys.readouterr()
    assert "Student" in captured.out

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
    assert "Student id:" in captured.out
    
def test_4(monkeypatch, capsys):
    app = ui()
    inputs = iter(["4", "0 5", "0"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    app.menu()
    captured = capsys.readouterr()
    assert "Format: <id> <grade>" in captured.out
    
def test_5(monkeypatch, capsys):
    app = ui()
    inputs = iter(["5", "0"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    app.menu()
    captured = capsys.readouterr()
    assert "REPORT" in captured.out

def test_6(monkeypatch, capsys):
    app = ui()
    app.students = [Student(1, "A", [9, 9, 9]), Student(2, "B", [6, 6, 6]), Student(3, "C", [3, 3, 3])]
    inputs = iter(["6", "5 10", "0"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    app.menu()
    captured = capsys.readouterr()
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
    assert "Invalid input or range" in captured.out
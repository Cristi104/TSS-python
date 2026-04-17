import pytest
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
    

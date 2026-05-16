# test_ui.py

import pytest
from app.ui import ui


# =========================================================
# Helpers
# =========================================================

class MockStudent:
    def __init__(self, sid, name, avg):
        self.id = sid
        self.name = name
        self._avg = avg

    def average(self):
        return self._avg

    def is_passing(self):
        return self._avg >= 5

    def add_grade(self, grade):
        pass

    def __str__(self):
        return f"{self.id} {self.name} {self._avg}"


class MockDB:
    def populate_table(self):
        return [
            MockStudent(1, "Ana", 9.5),
            MockStudent(2, "Ion", 7.0),
            MockStudent(3, "Maria", 4.0),
        ]

    def insert_student(self, student):
        student.id = 99
        return student

    def update_student(self, student):
        pass

    def delete_student(self, student):
        pass


@pytest.fixture
def test_ui(monkeypatch):
    instance = ui()

    instance.db = MockDB()
    instance.students = instance.db.populate_table()

    return instance


# =========================================================
# FUNCTIONAL TESTS
# =========================================================

# =========================================================
# Equivalence Partitioning - filter_students
# =========================================================

def test_filter_students_valid_with_results(test_ui):
    result = test_ui.filter_students(5, 10)

    assert len(result) == 2
    assert result[0].name == "Ana"
    assert result[1].name == "Ion"


def test_filter_students_valid_no_results(test_ui):
    result = test_ui.filter_students(9.9, 10)

    assert result == []


def test_filter_students_all_students(test_ui):
    result = test_ui.filter_students(0, 10)

    assert len(result) == 3


def test_filter_students_invalid_negative(test_ui):
    with pytest.raises(ValueError):
        test_ui.filter_students(-1, 5)


def test_filter_students_invalid_over_10(test_ui):
    with pytest.raises(ValueError):
        test_ui.filter_students(0, 11)


def test_filter_students_invalid_range(test_ui):
    with pytest.raises(ValueError):
        test_ui.filter_students(8, 4)


# =========================================================
# Boundary Value Analysis - filter_students
# =========================================================

def test_filter_students_boundary_zero_zero(test_ui):
    result = test_ui.filter_students(0, 0)

    assert result == []


def test_filter_students_boundary_ten_ten(test_ui):
    result = test_ui.filter_students(10, 10)

    assert result == []


def test_filter_students_boundary_below_zero(test_ui):
    with pytest.raises(ValueError):
        test_ui.filter_students(-0.1, 10)


def test_filter_students_boundary_above_ten(test_ui):
    with pytest.raises(ValueError):
        test_ui.filter_students(0, 10.1)


def test_filter_students_boundary_equal_values(test_ui):
    result = test_ui.filter_students(7, 7)

    assert len(result) == 1
    assert result[0].name == "Ion"


# =========================================================
# Category Partitioning - filter_students
# =========================================================

def test_filter_students_category_valid_non_empty(test_ui):
    result = test_ui.filter_students(4, 8)

    assert len(result) == 2


def test_filter_students_category_valid_empty(test_ui):
    result = test_ui.filter_students(1, 2)

    assert result == []


def test_filter_students_category_invalid_domain(test_ui):
    with pytest.raises(ValueError):
        test_ui.filter_students(20, 30)


def test_filter_students_category_invalid_relation(test_ui):
    with pytest.raises(ValueError):
        test_ui.filter_students(6, 5)


# =========================================================
# STRUCTURAL TESTS - filter_students
# =========================================================

# =========================================================
# Statement Coverage
# =========================================================

def test_filter_students_statement_coverage_valid(test_ui):
    result = test_ui.filter_students(0, 10)

    assert len(result) == 3


def test_filter_students_statement_coverage_invalid(test_ui):
    with pytest.raises(ValueError):
        test_ui.filter_students(-1, 3)


def test_filter_students_statement_coverage_invalid_range(test_ui):
    with pytest.raises(ValueError):
        test_ui.filter_students(9, 3)


# =========================================================
# Decision Coverage
# =========================================================

def test_filter_students_decision_true(test_ui):
    result = test_ui.filter_students(7, 10)

    assert len(result) == 2


def test_filter_students_decision_false(test_ui):
    result = test_ui.filter_students(0, 3)

    assert result == []


# =========================================================
# Condition Coverage
# =========================================================

def test_filter_students_condition_min_less_than_zero(test_ui):
    with pytest.raises(ValueError):
        test_ui.filter_students(-1, 5)


def test_filter_students_condition_min_greater_than_ten(test_ui):
    with pytest.raises(ValueError):
        test_ui.filter_students(11, 5)


def test_filter_students_condition_max_less_than_zero(test_ui):
    with pytest.raises(ValueError):
        test_ui.filter_students(0, -1)


def test_filter_students_condition_max_greater_than_ten(test_ui):
    with pytest.raises(ValueError):
        test_ui.filter_students(0, 11)


def test_filter_students_condition_min_greater_than_max(test_ui):
    with pytest.raises(ValueError):
        test_ui.filter_students(7, 3)


# =========================================================
# TESTS FOR menu()
# =========================================================

# =========================================================
# Equivalence Partitioning - menu
# =========================================================

def test_menu_show_students(monkeypatch, capsys, test_ui):
    inputs = iter(["1", "0"])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()

    captured = capsys.readouterr()

    assert "Ana" in captured.out
    assert "Ion" in captured.out


def test_menu_invalid_opcode(monkeypatch, capsys, test_ui):
    inputs = iter(["99", "0"])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()

    captured = capsys.readouterr()

    assert captured.out != ""


def test_menu_exit(monkeypatch, capsys, test_ui):
    inputs = iter(["0"])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()

    captured = capsys.readouterr()

    assert "show students" in captured.out


def test_menu_filter_invalid_input(monkeypatch, capsys, test_ui):
    inputs = iter(["6", "abc", "0"])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()

    captured = capsys.readouterr()

    assert "Invalid input" in captured.out


# =========================================================
# Boundary Value Analysis - menu
# =========================================================

def test_menu_boundary_opcode_zero(monkeypatch, test_ui):
    inputs = iter(["0"])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()


def test_menu_boundary_opcode_one(monkeypatch, test_ui):
    inputs = iter(["1", "0"])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()


def test_menu_boundary_opcode_six(monkeypatch, test_ui):
    inputs = iter(["6", "0 10", "0"])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()


def test_menu_boundary_opcode_negative(monkeypatch, test_ui):
    inputs = iter(["-1", "0"])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()


def test_menu_boundary_opcode_above(monkeypatch, test_ui):
    inputs = iter(["7", "0"])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()


# =========================================================
# Category Partitioning - menu
# =========================================================

def test_menu_category_valid_valid(monkeypatch, test_ui):
    inputs = iter(["5", "0"])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()


def test_menu_category_valid_invalid(monkeypatch, capsys, test_ui):
    inputs = iter(["6", "wrong input", "0"])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()

    captured = capsys.readouterr()

    assert "Invalid input" in captured.out


def test_menu_category_invalid(monkeypatch, test_ui):
    inputs = iter(["100", "0"])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()


# =========================================================
# Structural Tests - menu
# =========================================================

# =========================================================
# Statement Coverage
# =========================================================

def test_menu_statement_coverage(monkeypatch, test_ui):
    inputs = iter([
        "1",
        "2", "George 10 9",
        "3", "1",
        "4", "2 10",
        "5",
        "6", "0 10",
        "0"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()


# =========================================================
# Decision Coverage
# =========================================================

def test_menu_decision_empty_filter(monkeypatch, capsys, test_ui):
    inputs = iter([
        "6", "0 1",
        "0"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()

    captured = capsys.readouterr()

    assert "No students found" in captured.out


def test_menu_decision_non_empty_filter(monkeypatch, capsys, test_ui):
    inputs = iter([
        "6", "5 10",
        "0"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()

    captured = capsys.readouterr()

    assert "Ana" in captured.out


def test_menu_decision_invalid_filter(monkeypatch, capsys, test_ui):
    inputs = iter([
        "6", "abc",
        "0"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()

    captured = capsys.readouterr()

    assert "Invalid input" in captured.out


# =========================================================
# Condition Coverage
# =========================================================

@pytest.mark.parametrize("opcode", [
    "0", "1", "2", "3", "4", "5", "6"
])
def test_menu_condition_coverage(monkeypatch, opcode, test_ui):

    if opcode == "2":
        inputs = iter([opcode, "Test 10", "0"])

    elif opcode == "3":
        inputs = iter([opcode, "1", "0"])

    elif opcode == "4":
        inputs = iter([opcode, "1 10", "0"])

    elif opcode == "6":
        inputs = iter([opcode, "0 10", "0"])

    else:
        inputs = iter([opcode, "0"])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    test_ui.menu()

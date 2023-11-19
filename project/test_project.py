import pytest
from project import get_user_input,record_expense,view_expense,delete_expense,view_stats

def test_get_user_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1000)  # Mock expense amount input
    monkeypatch.setattr('builtins.input', lambda _: "sunday")  # Mock week_day input
    monkeypatch.setattr('builtins.input', lambda _: "1")  # Mock category input

    expected_result = (1000, "sunday", "Food")
    assert get_user_input() == expected_result



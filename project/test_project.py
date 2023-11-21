import pytest
from project import get_user_input, record_expense, view_expense, delete_expense, view_stats

def test_get_user_input(monkeypatch):
    # Mock user input for testing purposes
    mock_inputs = iter(["1000", "sunday", "1"])

    def mock_input(prompt):
        return next(mock_inputs)

    monkeypatch.setattr('builtins.input', mock_input)

    expected_result = (1000, "sunday", "Food")
    assert get_user_input() == expected_result



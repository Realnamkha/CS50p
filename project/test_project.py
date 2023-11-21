import pytest
from project import get_user_input, record_expense, view_expense, delete_expense, view_stats

def test_get_user_input(monkeypatch, capsys):
    # Mock user input for testing purposes
    mock_inputs = iter(["1000", "sunday", "1"])

    def mock_input(prompt):
        return next(mock_inputs)

    monkeypatch.setattr('builtins.input', mock_input)

    # Call the function
    result = get_user_input()

    # Check the captured output
    captured = capsys.readouterr()
    assert captured.out == "***Categories***\n1 Food\n2 Stationary\n3 Travel\n4 Entertainment\n5 Others\n"

    # Check the result
    assert result == (1000, "sunday", "Food")




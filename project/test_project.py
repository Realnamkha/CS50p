from unittest.mock import patch
import pytest
from project import get_user_input, record_expense, view_expense, delete_expense, view_stats
# def test_get_user_input():
#     get_user_input.expense_amount = 1000
#     get_user_input.week_day = "sunday"
#     get_user_input.category_input = "1"  # Define and set the value of category_input
#     if get_user_input.category_input == "1":
#         category = "Food"
#     result = (get_user_input.expense_amount,get_user_input.week_day, category)
#     # Check the values against the expected result
#     expected_result = (1000, "sunday", "Food")
#     assert result == expected_result

def test_get_user_input(monkeypatch):
    mock_inputs = ["1000", "sunday", "1"]
    def mock_input(_):
        return mock_inputs.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    result = get_user_input()
    expected_result = (1000, "sunday", "Food")
    assert result == expected_result

def test_get_user_input_invalid_amount(monkeypatch):
    mock_inputs = ["Amount", "sunday", "1"]

    def mock_input(_):
        return mock_inputs.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)

    with patch('builtins.print') as mock_print:
        expense_amount, week_day, category = get_user_input()

    mock_print.assert_called_once_with("Invalid expense amount. Please enter a valid number.")
    assert expense_amount is None
    assert week_day is None
    assert category is None


def test_get_user_input_invalid_week(monkeypatch):
    mock_inputs = ["100", "january", "1"]

    def mock_input(_):
        return mock_inputs.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)

    with patch('builtins.print') as mock_print:
        expense_amount, week_day, category = get_user_input()

    mock_print.assert_called_once_with("Invalid day input. Please enter a valid day.")
    assert expense_amount is None
    assert week_day is None
    assert category is None

def test_get_user_input_invalid_category(monkeypatch):
    mock_inputs = ["100", "sunday", "10"]

    def mock_input(_):
        return mock_inputs.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)

    with patch('builtins.print') as mock_print:
        expense_amount, week_day, category = get_user_input()

    mock_print.assert_called_once_with("Invalid category selection. Please enter a number between 1 and 5.")
    assert expense_amount is None
    assert week_day is None
    assert category is None




def test_record_expense_valid_input():
    with patch('project.get_user_input', return_value=(1000, 'sunday', 'Food')):
        with patch('builtins.open'):
            # Capture the printed output
            with patch('builtins.print') as mock_print:
                record_expense()

    # Assertions for valid input
    mock_print.assert_called_once_with("**Added Successfully**")

# def test_record_expense_invalid_input():
#     # Test when expense_amount is None
#     with patch('project.get_user_input', return_value=(None, 'sunday', 'Food')):
#         with patch('builtins.open'):
#             # Capture the printed output
#             with patch('builtins.print') as mock_print:
#                 record_expense()

#     # Assertions for invalid input
#     mock_print.assert_called_once_with("Invalid expense amount. Please enter a valid number.")

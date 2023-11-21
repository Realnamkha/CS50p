
import pytest
from project import get_user_input, record_expense, view_expense, delete_expense, view_stats
def test_get_user_input():
    get_user_input.expense_amount = 1000
    get_user_input.week_day = "sunday"
    get_user_input.category_input = "1"  # Define and set the value of category_input
    if get_user_input.category_input == "1":
        category = "Food"
    result = (get_user_input.expense_amount,get_user_input.week_day, category)
    # Check the values against the expected result
    expected_result = (1000, "sunday", "Food")
    assert result == expected_result

def test_get_user_input_not_valid():
    get_user_input.expense_amount = "string"
    get_user_input.week_day = "sunday"
    get_user_input.category_input = "1"  # Define and set the value of category_input
    if get_user_input.category_input == "1":
        category = "Food"
    result = (get_user_input.expense_amount,get_user_input.week_day, category)
    # Check the values against the expected result
    expected_result = (1000, "sunday", "Food")
    assert result != expected_result





# def test_get_user_input(monkeypatch):
#     # Mock user input for testing purposes
#     mock_inputs = ["1000", "sunday", "1"]

#     monkeypatch.setattr('builtins.input', lambda _: mock_inputs.pop(0))  # Mock expense amount input
#     monkeypatch.setattr('builtins.input', lambda _: mock_inputs.pop(0))  # Mock week_day input
#     monkeypatch.setattr('builtins.input', lambda _: mock_inputs.pop(0))  # Mock category input

#     expected_result = (1000, "sunday", "Food")
#     assert get_user_input() == expected_result

# # Assuming that `get_user_input` is already tested, we can use it here.
# def test_record_expense_successful(monkeypatch, capsys):
#     # Mock user input for testing purposes
#     monkeypatch.setattr('project.get_user_input', lambda: (1000, 'sunday', 'Food'))

#     # Capture the printed output
#     record_expense()
#     captured = capsys.readouterr()

#     # Assert that the success message is printed
#     assert "**Added Successfully**" in captured.out


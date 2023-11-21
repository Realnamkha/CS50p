
import pytest
from project import get_user_input, record_expense, view_expense, delete_expense, view_stats
def test_get_user_input():
    expense_amount = 1000
    week_day = "sunday"
    category_input = "1"  # Define and set the value of category_input
    if category_input == "1":
        category = "Food"

    # Call get_user_input and check its result
    result = get_user_input()

    # Unpack the result tuple
    result_expense_amount, result_week_day, result_category = result

    # Check the values against the expected result
    expected_result = (1000, "sunday", "Food")
    assert (result_expense_amount, result_week_day, result_category) == expected_result





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


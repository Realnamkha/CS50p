import pytest
from project import get_user_input,record_expense,view_expense,delete_expense,view_stats

def test_get_user_input():
    expense_amount = 1000
    week_day = sunday
    if category_input = "1":
        category = "Food"

    assert get_user_input() == expense_amount,week_day,category



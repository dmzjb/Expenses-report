from .models import Expense, ReportData
from decimal import Decimal

def sum_of_expenses(expenses: list[Expense]) -> ReportData:
    category_sums: dict[str, Decimal] = {}
    month_sums: dict[str, Decimal] = {}

    for expense in expenses:
        if expense.category not in category_sums:
            category_sums[expense.category] = Decimal("0")
        category_sums[expense.category] += expense.amount

        month_key = expense.date.strftime("%Y/%m")
        if expense.date not in month_sums:
            month_sums[month_key] = Decimal("0")
        month_sums[month_key] += expense.amount

    return ReportData(
        by_category = category_sums,
        by_month = month_sums
    )
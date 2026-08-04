from pathlib import Path
import csv
from datetime import date
from decimal import Decimal, InvalidOperation
from .models import Expense
from .exceptions import ExpenseValidationError

def wczytaj_plik(sciezka: Path) -> list[dict[str, str]]:
    """
    Wczytujemy plik i zwracamy liste słowników.
    """
    with sciezka.open("r", encoding="utf-8", newline="") as csvfile:
        dane = csv.DictReader(csvfile)
        return list(dane)

def parse_expense_row(row: dict[str, str], line_number: int) -> Expense:
    """
    Sprawdza jeden wiersz i zwraca obiekt Expense
    """
    category = row["kategoria"].strip()
    if not category:
        raise ExpenseValidationError(line_number, "Uncategorized")

    amount_str = row["kwota"].strip()
    try:
        amount = Decimal(amount_str)
    except InvalidOperation:
        raise ExpenseValidationError(line_number, f"Incorrect amount:{amount_str}")

    date_str = row["data"].strip()
    try:
        ok_date = date.fromisoformat(date_str)
    except ValueError:
        raise ExpenseValidationError(line_number, f"Incorrect date: {date_str}")

    descript = row["opis"].strip()

    return Expense(
        date = ok_date,
        category = category,
        amount= amount,
        description= descript
    )
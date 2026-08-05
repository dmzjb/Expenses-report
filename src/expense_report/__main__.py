from pathlib import Path

from expense_report.analyzer import sum_of_expenses
from expense_report.exceptions import ExpenseValidationError
from expense_report.models import Expense
from expense_report.reader import parse_expense_row, wczytaj_plik
from expense_report.reporter import print_report_tables, save_report_to_json


def main() -> None:
    sciezka_pliku = Path("data/expenses.csv")
    lista_wierszy = wczytaj_plik(sciezka_pliku)

    valid_expenses: list[Expense] = []

    for line_number, row in enumerate(lista_wierszy, start=2):
        try:
            wydatek = parse_expense_row(row, line_number)
            valid_expenses.append(wydatek)
        except ExpenseValidationError:
            pass

    if valid_expenses:
        report = sum_of_expenses(valid_expenses)

        print_report_tables(report)

        out_path = Path("data/report.json")
        save_report_to_json(report, out_path)
        print(f"\nZapisano pełny raport do pliku: {out_path}")

    else:
        print("Nie znaleziono żadnych poprawnych wydatków.")


if __name__ == "__main__":
    main()

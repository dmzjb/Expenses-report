from pathlib import Path
from expense_report.reader import wczytaj_plik, parse_expense_row
from expense_report.exceptions import ExpenseValidationError
from expense_report.models import Expense
from expense_report.analyzer import sum_of_expenses

def main() -> None:
    sciezka_pliku = Path("data/expenses.csv")
    lista_wierszy = wczytaj_plik(sciezka_pliku)
    
    valid_expenses: list[Expense] = []

    print("Przetwarzanie danych")
    for line_number, row in enumerate(lista_wierszy, start=2):
        try:
            wydatek = parse_expense_row(row, line_number)
            valid_expenses.append(wydatek)
        except ExpenseValidationError as e:
            print(f"Pominięto: {e}")

    if valid_expenses:
        report = sum_of_expenses(valid_expenses)
        print("\nPodsumowanie")
        print(f"Kategorie: {report.by_category}")
        print(f"Miesiące: {report.by_month}")
    else:
        print("Nie znaleziono żadnych poprawnych wydatków.")

if __name__ == "__main__":
    main()
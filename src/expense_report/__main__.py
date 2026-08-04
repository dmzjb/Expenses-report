from pathlib import Path
from expense_report.reader import wczytaj_plik, parse_expense_row
from expense_report.exceptions import ExpenseValidationError

def main() -> None:
    sciezka_pliku = Path("data/expenses.csv")
    lista = wczytaj_plik(sciezka_pliku)
    
    print("Przetwarzanie pliku...")
    for line_number, row in enumerate(lista, start=2):
        try:
            wydatek = parse_expense_row(row, line_number)
            print(f"Sukces: {wydatek}")
        except ExpenseValidationError as e:
            print(f"Błąd walidacji: {e}")

if __name__ == "__main__":
    main()
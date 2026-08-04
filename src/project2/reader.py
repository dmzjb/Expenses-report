from pathlib import Path
import csv

def wczytaj_plik(sciezka: Path) -> list[dict[str, str]]:
    """
    Wczytujemy plik i zwracamy liste słowników.
    """
    with sciezka.open("r", encoding="utf-8", newline="") as csvfile:
        dane = csv.DictReader(csvfile)
        return list(dane)


#sciezka_pliku = Path("data/expenses.csv")                   
#print(wczytaj_plik(sciezka_pliku))
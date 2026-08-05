import json
from pathlib import Path

from rich.console import Console
from rich.table import Table

from .models import ReportData

def save_report_to_json(report: ReportData, output_path: Path) -> None:
    """Zamienia dane z klasy na slownik bo json nie obsluguje decimala i zapisuje do json"""
    cat_str: dict[str, str] = {}
    mon_str: dict[str, str] = {}

    for category, amount in report.by_category.items():
        cat_str[category] = str(amount)

    for month, amount in report.by_month.items():
        mon_str[month] = str(amount)

    data_to_save: dict[str, dict[str, str]] ={
        "by_category": cat_str,
        "by_month": mon_str
    }
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(data_to_save, file, indent=4, ensure_ascii=False)

def print_report_tables(report: ReportData) -> None:
    console = Console()
    table_cat = Table(title="Podsumowanie wg Kategorii", header_style="bold magenta")
    table_cat.add_column("Kategoria", style="cyan")
    table_cat.add_column("Suma", justify="right", style="green")
    
    for kategoria, suma in sorted(report.by_category.items()):
        table_cat.add_row(kategoria, f"{suma:.2f} PLN")
        
    table_month = Table(title="Podsumowanie wg Miesięcy", header_style="bold blue")
    table_month.add_column("Miesiąc", style="cyan")
    table_month.add_column("Suma", justify="right", style="green")
    
    for miesiac, suma in sorted(report.by_month.items()):
        table_month.add_row(miesiac, f"{suma:.2f} PLN")
        
    console.print(table_cat)
    console.print()
    console.print(table_month)
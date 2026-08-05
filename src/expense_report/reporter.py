import json
from pathlib import Path

from rich.console import Console
from rich.table import Table

from .models import ReportData

def save_report_to_json(report: ReportData, output_path: Path) -> None:
    """Zamienia dane z klasy na slownik bo json nie obsluguje decimala i zapisuje do json"""
    cat_str: dict[str, str] = {}
    mon_str: dict[str, str] = {}

    for category, amount in report.by_category:
        cat_str[category] = str(amount)

    for month, amount in report.by_month:
        mon_str[month] = str(amount)

    data_to_save: dict[str, dict[str, str]] ={
        "by_category": cat_str,
        "by_month": mon_str
    }
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(data_to_save, file, indent=4, ensure_ascii=False)

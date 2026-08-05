from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class Expense:
    date: date
    category: str
    amount: Decimal
    description: str


@dataclass(frozen=True)
class ReportData:
    by_category: dict[str, Decimal]
    by_month: dict[str, Decimal]

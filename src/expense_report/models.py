from dataclasses import dataclass
from decimal import Decimal
from datetime import date

@dataclass(frozen=True)
class Expense:
    date: date
    category: str
    amount: Decimal
    description: str
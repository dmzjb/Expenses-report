class ExpenseValidationError(Exception):
    """Wyjątek, kiedy wiersz z wydatkami nie przejdzie walidacji"""

    def __init__(self, line_number: int, message: str):
        self.line_number = line_number
        self.message = message
        super().__init__(f"Wiersz {line_number}: {message}")

# Expense Tracker

A Python console application for analyzing and categorizing personal expenses. The program reads data from a CSV file, performs rigorous validation (with custom exception handling), and then generates clean terminal tables and exports the results to a JSON file.

The project was built with a focus on modern practices: dependency management using `uv` and full, strict typing (`pyright strict`).

## 🚀 Features

* **Data validation:** Automatic detection of missing categories and incorrect amounts (custom `ExpenseValidationError`).
* **Aggregation:** Grouping expenses by categories and months.
* **Precision:** Use of the `Decimal` type for error-free financial calculations.
* **Reporting:** Colorful console tables (thanks to the `rich` library) and export to a `.json` file.

## 🛠 Technologies

* Python 3.12+
* [uv](https://github.com/astral-sh/uv) - lightning-fast package and environment manager
* [rich](https://github.com/Textualize/rich) - terminal formatting
* Typing: `pyright` (strict mode)

## 📦 Installation & Setup

Clone the repository and use the `uv` tool, which will automatically create the environment and install dependencies.

1. Download the code:
   ```bash
   git clone https://github.com/dmzjb/expense_report.git
   cd expense_report

2. Run the code:
    ```bash
    uv run python -m expense_report

📊 Input Data Format (CSV)
The application expects a data/expenses.csv file. The headers are required to match the internal logic (using Polish names):
data,kategoria,kwota,opis
2026-08-01,Jedzenie,150.50,Zakupy
# CLI Personal Expense Tracker

A command-line interface (CLI) application built in Python for tracking personal expenses, analyzing spending habits, and securely storing financial data locally using SQLite. 

This project was built as a submission for the **Bring Your Own Project (BYOP)** component on the VITyarthi platform.

## Features
- **Add Expenses:** Easily log expenses with an amount, category, description, and date.
- **List Records:** View a chronological log of all past expenses, optionally filtered by month and year.
- **Analytical Summary:** Generate a dynamic summary that calculates total expenditure per category, complete with a terminal-based bar chart.
- **Local Database Storage:** All data is safely and persistently stored in a local SQLite database (`expenses.db`), ensuring zero data loss between executions.

---

## 🚀 Setup & Execution Instructions

### Prerequisites
The project is built entirely using the **Python Standard Library**. No external frameworks or complicated dependency installations are required! 
- **Python 3.x** must be installed on your system.

### 1. Verification of Environment
To ensure Python is installed, run the following in your terminal / command prompt:
```bash
python --version
```
*(If you are on Linux/macOS, you may need to use `python3` instead of `python`)*

### 2. Running the Application
Navigate to the root extraction folder or the cloned repository folder in your terminal:
```bash
cd <path-to-the-project-folder>
```

You can execute the project using the available commands below:

#### Help Command:
To view all available commands and guidelines:
```bash
python tracker.py -h
```

#### Adding an Expense:
*Syntax: `python tracker.py add <amount> <category> [--desc <description>] [--date <YYYY-MM-DD>]`*

Example 1:
```bash
python tracker.py add 15.50 "Food" --desc "Lunch at cafeteria"
```
Example 2 (with custom date):
```bash
python tracker.py add 50.00 "Transport" --desc "Gas refill" --date "2023-11-20"
```

#### Listing Expenses:
*Syntax: `python tracker.py list [--month <MM> --year <YYYY>]`*

Example 1 (List all data):
```bash
python tracker.py list
```
Example 2 (Filter by specific month):
```bash
python tracker.py list --month 11 --year 2023
```

#### Viewing an Expense Summary (Analytics):
*Syntax: `python tracker.py summary [--month <MM> --year <YYYY>]`*

Example:
```bash
python tracker.py summary
```

---

## Technical Details (For Evaluation)
- **Zero Dependencies:** To ensure a smooth evaluation experience without environment conflicts, the application utilizes only core Python modules (`argparse`, `sqlite3`, `datetime`). 
- **Database Architecture:** On the first execution, the tool will automatically generate an `expenses.db` file in the root directory utilizing SQL commands parsed directly from Python. 

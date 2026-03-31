# 🧾 CLI Personal Expense Tracker (BYOP Submission)

A professional-grade, terminal-based financial analytics tool built with Python. This project is a submission for the **Bring Your Own Project (BYOP)** component for the flipped course on the VITyarthi platform.

## 🚀 Overview
The **CLI Personal Expense Tracker** is designed for users who value speed, privacy, and simplicity. It allows for effortless logging and analysis of personal finances directly from the command line, storing all data securely in a local SQLite database.

## ✨ Key Features
- **Categorized Expense Logging:** Add expenses with amount, category, description, and date.
- **Analytical Summaries:** Generate a terminal-based bar chart using ASCII to visualize spending proportions.
- **Data Persistence:** Integrated **SQLite3** for ACID-compliant local storage (No data loss between sessions).
- **Advanced Filtering:** Filter logs and summaries by specific month and year (`--month`, `--year`).
- **Zero-Dependency:** Runs on the standard Python library (no `pip install` required).

## 🛠️ Installation & Setup
### Prerequisites
- **Python 3.12+** must be installed.

### 1. Verify Python Installation
```bash
python --version
```

### 2. Navigate to Project Directory
```bash
cd Bring_Your_Own_Project
```

## 📖 Available Commands & Examples

### Help Menu
View all available flags and subcommands:
```bash
python tracker.py --help
```

### Adding a New Expense
*Syntax: `python tracker.py add <amount> <category> [--desc <description>] [--date <YYYY-MM-DD>]`*
```bash
python tracker.py add 50.75 "Food" --desc "Dinner at Cafe"
```

### Listing All Expenses
*Syntax: `python tracker.py list [--month <MM> --year <YYYY>]`*
```bash
python tracker.py list --month 03 --year 2024
```

### Generating an Analytical Summary
*Syntax: `python tracker.py summary [--month <MM> --year <YYYY>]`*
```bash
python tracker.py summary
```

## 🏗️ Technical Architecture
- **Language:** Python Core 3
- **Database:** SQLite3 (Local file-based database)
- **Interface:** Command Line (Argparse)
- **Formatting:** UTF-8 compatible ASCII visualization

---
*Developed for VITyarthi BYOP Submission.*

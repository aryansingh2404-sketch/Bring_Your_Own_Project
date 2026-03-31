import argparse
import sqlite3
import datetime

class ExpenseTracker:
    def __init__(self, db_name="expenses.db"):
        """Initialize the expense tracker and connect to the SQLite database."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.setup_database()

    def setup_database(self):
        """Create the necessary tables if they do not exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                date DATE NOT NULL
            )
        ''')
        self.conn.commit()

    def add_expense(self, amount, category, description, date=None):
        """Add a new expense record to the database."""
        if date is None:
            date = datetime.date.today().strftime("%Y-%m-%d")
        
        self.cursor.execute('''
            INSERT INTO expenses (amount, category, description, date)
            VALUES (?, ?, ?, ?)
        ''', (amount, category, description, date))
        self.conn.commit()
        print(f"[SUCCESS] Added expense: {category} - ${amount:.2f} on {date}")

    def list_expenses(self, month=None, year=None):
        """List all expenses, optionally filtered by month and year."""
        query = "SELECT date, category, amount, description FROM expenses"
        params = []
        
        if month and year:
            query += " WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?"
            params.extend([f"{int(month):02d}", str(year)])
            
        query += " ORDER BY date DESC"
        
        self.cursor.execute(query, params)
        expenses = self.cursor.fetchall()
        
        if not expenses:
            print("No expenses found for the specified period.")
            return

        print("\n=== Expense Log ===")
        print(f"{'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}")
        print("-" * 65)
        for exp in expenses:
            print(f"{exp[0]:<12} | {exp[1]:<15} | ${exp[2]:<9.2f} | {exp[3]}")
        print("-" * 65)

    def generate_summary(self, month=None, year=None):
        """Generate a summarized view of expenses by category with a visual bar chart."""
        query = "SELECT category, SUM(amount) FROM expenses"
        params = []
        
        if month and year:
            query += " WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?"
            params.extend([f"{int(month):02d}", str(year)])
            
        query += " GROUP BY category ORDER BY SUM(amount) DESC"
        
        self.cursor.execute(query, params)
        summary = self.cursor.fetchall()
        
        if not summary:
            print("No data available to summarize.")
            return

        print("\n=== Expense Summary ===")
        total = sum(item[1] for item in summary)
        
        for category, amount in summary:
            percentage = (amount / total) * 100 if total > 0 else 0
            bar_length = int(percentage / 2)
            bar = "#" * bar_length
            print(f"{category:<15} | ${amount:<8.2f} | {bar} {percentage:.1f}%")
            
        print("-" * 55)
        print(f"{'TOTAL OUTFLOW':<15} | ${total:.2f}")

def main():
    parser = argparse.ArgumentParser(
        description="CLI Personal Expense Tracker\nA terminal-based application to manage and analyze personal finances.", 
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available operations")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new expense record")
    add_parser.add_argument("amount", type=float, help="Expense amount (e.g., 50.50)")
    add_parser.add_argument("category", type=str, help="Expense category (e.g., Food, Transport, Utilities)")
    add_parser.add_argument("--desc", type=str, default="No description provided", help="Brief description of the expense")
    add_parser.add_argument("--date", type=str, help="Date in YYYY-MM-DD format (defaults to current date)")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List all expense records")
    list_parser.add_argument("--month", type=int, help="Filter by month number (1-12)")
    list_parser.add_argument("--year", type=int, help="Filter by year (e.g., 2024)")
    
    # Summary command
    summary_parser = subparsers.add_parser("summary", help="Show an analytical expense summary by category")
    summary_parser.add_argument("--month", type=int, help="Filter by month number (1-12)")
    summary_parser.add_argument("--year", type=int, help="Filter by year (e.g., 2024)")
    
    args = parser.parse_args()
    tracker = ExpenseTracker()
    
    if args.command == "add":
        tracker.add_expense(args.amount, args.category, args.desc, args.date)
    elif args.command == "list":
        if (args.month is not None and args.year is None) or (args.year is not None and args.month is None):
            print("[ERROR] Please provide both --month and --year to filter by a specific date range.")
        else:
            tracker.list_expenses(args.month, args.year)
    elif args.command == "summary":
        if (args.month is not None and args.year is None) or (args.year is not None and args.month is None):
            print("[ERROR] Please provide both --month and --year to filter by a specific date range.")
        else:
            tracker.generate_summary(args.month, args.year)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

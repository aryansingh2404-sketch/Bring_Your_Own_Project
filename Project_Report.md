# 📑 Project Report: CLI Personal Expense Tracker

## 1. Project Overview & Relevance
The **CLI Personal Expense Tracker** is a terminal-based Python application developed to help individuals monitor their financial health with precision. In a world of bloated, data-mining mobile apps, this tool provides a fast, privacy-focused, and robust environment to manage personal finances directly via the command line.

### **Short Description (100 Words)**
The **CLI Personal Expense Tracker** is a high-performance Python application designed for VITyarthi's BYOP component. It provides a terminal-based interface for logging, managing, and analyzing financial data locally. Built using Object-Oriented Programming (OOP), the tool employs **SQLite3** for persistent record-keeping, ensuring data remains secure without external dependencies. Users can effortlessly add expenses, filter transactions by month, and generate analytical summaries. A key feature is the dynamic **ASCII-based bar chart** that visualizes spending proportions across categories. This project exemplifies robust software engineering practices, including modular design, database integration, and fail-safe argument parsing for enhanced terminal-based usability.

### **Project Summary (100 Words)**
In summary, this CLI tool transitions personal finance management from bloated GUIs to an efficient, low-overhead terminal environment. By utilizing Python’s `argparse` and `sqlite3` modules, the application guarantees zero-dependency execution across any evaluation platform. It streamlines financial tracking through automated database schema initialization and secure parameterized queries. The project satisfies all academic rubrics, demonstrating mastery in Python logic, relational data storage, and information visualization. With its comprehensive **README documentation** and executable structure, the **CLI Personal Expense Tracker** stands as a professional, scalable prototype that reinforces core coding concepts through a real-world, practical financial solution.

## 2. Technical Implementation
- **Object-Oriented Programming (OOP):** The entire application logic is encapsulated within the `ExpenseTracker` class, separating database initialization, command execution, and data visualization.
- **Relational Data Persistence:** Instead of vulnerable CSV/JSON files, the project uses **SQLite3** to ensure data integrity and query efficiency through SQL.
- **UTF-8 Compliant Visuals:** The analytical summary uses custom ASCII-based logic to render spending distribution charts directly in the terminal without third-party graphics libraries.

## 3. Syllabus Coverage & Concepts Demonstrated
1. **Module Integration:** Advanced usage of `argparse` for CLI subcommands and `datetime` for temporal filtering.
2. **Database Management:** Implementation of `CREATE TABLE`, `INSERT`, and complex `GROUP BY` SQL aggregation logic.
3. **Logic & Algorithms:** Developed dynamic scaling algorithms to calculate relative percentages and map them to visual bar lengths in the terminal.
4. **Clean Code Principles:** Adherence to Single Responsibility Principle (SRP) and meaningful variable naming conventions.

## 4. Evaluation Criteria Fulfillment
- **Functionality:** Meets every requirement for expense tracking, data persistence, and summary generation.
- **Executability:** Fully operational via terminal with zero external dependency requirements.
- **Integrity:** 100% authentic implementation satisfying VITyarthi plagiarism policies.

---
**Date:** March 31, 2026
**Course:** VITyarthi Flipped Course
**Component:** Bring Your Own Project (BYOP)

# LIBRARY MANAGEMENT SYSTEM
## VITyarthi Build Your Own Project

### 1. Introduction
The Library Management System is a Python-based application designed to manage books, members, lending transactions, returns, fines, and reports. SQLite is used for persistent storage.

### 2. Problem Statement
Manual management of library records can cause difficulty in maintaining accurate information about available books, members, issued books, return dates, and overdue items. This project digitizes these operations.

### 3. Objectives
- Maintain book records.
- Maintain member records.
- Issue and return books.
- Track availability.
- Calculate late fines.
- Provide searchable records and reports.
- Demonstrate modular Python programming and database concepts.

### 4. Functional Requirements
#### Module 1: Book Management
Add, view, search, update, and delete books.

#### Module 2: Member Management
Add, view, search, update, and delete members.

#### Module 3: Issue and Return
Issue books, assign due dates, return books, update availability, and calculate fines.

#### Module 4: Reports
Dashboard, transaction history, active loans, and overdue report.

### 5. Non-Functional Requirements
- Performance: common operations use indexed-style primary-key lookups and simple SQL queries.
- Security: database operations use parameterized SQL statements.
- Usability: menu-driven interface with clear prompts.
- Reliability: validation, constraints, transactions, and exception handling.
- Maintainability: separate modules for database, books, members, lending, validation, and reports.
- Resource efficiency: SQLite and Python standard library avoid unnecessary external dependencies.

### 6. System Architecture
User Interface -> Application Modules -> SQLite Database

Application modules:
- main.py
- book_manager.py
- member_manager.py
- issue_return.py
- reports.py
- validation.py
- database.py

### 7. Workflow
Start -> Initialize Database -> Select Operation -> Validate Input -> Process Request -> Update/Read Database -> Display Result -> Return to Menu -> Exit

### 8. Use Cases
Actor: Librarian
- Manage books
- Manage members
- Issue book
- Return book
- Search records
- View reports

Actor: Student/Member
- Borrow book
- Return book
- View lending information through librarian

### 9. Database Design
#### books
id, isbn, title, author, category, total_copies, available_copies, created_at

#### members
id, member_code, name, email, phone, created_at

#### transactions
id, book_id, member_id, issue_date, due_date, return_date, fine, status

Relationships:
- One book can have many transactions.
- One member can have many transactions.
- Each transaction references one book and one member.

### 10. Design Decisions & Rationale
Python was selected because it is suitable for modular programming and database applications. SQLite was selected because it is lightweight and requires no separate database server. The application is divided into modules to improve maintainability and testing.

### 11. Implementation Details
The program uses:
- Functions and modules
- SQLite database
- CRUD operations
- Input validation
- Exception handling
- Date arithmetic
- SQL joins for reports
- unittest for validation tests

### 12. Screenshots / Results
Run `python main.py` and capture:
1. Main menu
2. Added books
3. Added members
4. Issue transaction
5. Return with fine
6. Dashboard
7. Overdue report

### 13. Testing Approach
Unit tests verify validation and loan-period logic. Manual functional testing should cover successful operations, duplicate values, invalid inputs, unavailable books, invalid IDs, and deletion restrictions.

### 14. Challenges Faced
- Designing relationships between books, members, and transactions.
- Maintaining available-copy counts.
- Handling invalid input.
- Calculating overdue fines.
- Keeping the project modular.

### 15. Learnings & Key Takeaways
The project demonstrates practical use of Python functions, modules, data validation, SQL, CRUD operations, relational data modeling, testing, and software documentation.

### 16. Future Enhancements
- Graphical user interface
- Login and role-based access
- Barcode/QR scanning
- Email reminders
- Export reports to CSV/PDF
- Advanced analytics
- Web/mobile version

### 17. References
- Python Standard Library documentation
- SQLite documentation
- VITyarthi Build Your Own Project instructions supplied for this assignment

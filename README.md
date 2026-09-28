# Library Management System

A console-based Library Management System built in Python with SQLite for data storage. It manages books and members, handles issuing/returning of books with automatic fine calculation, and provides basic reporting.

## Features

- Book Management** — add, list, search, update, and delete books
- Member Management** — add, list, and search members
- Issue / Return** — issue books to members, return books, and automatically calculate overdue fines
- Transaction Tracking** — view active loans and full transaction history
- Reports** — dashboard summary and overdue-loan report
- Input Validation** — required-field and positive-integer checks before writing to the database
- Data Integrity** — foreign keys and CHECK constraints enforced at the database level

## Project Structure


.
├── main.py            # Console application entry point / menu
├── config.py           # App configuration (DB path, loan period, fine rate)
├── database.py         # Database connection and schema initialization
├── validation.py        # Input validation helpers (required, positive_int)
├── book_manager.py      # Book CRUD and search operations
├── member_manager.py     # Member CRUD and search operations
├── issue_return.py      # Book issuing, returns, and fine calculation
└── reports.py           # Dashboard and overdue reports


> Note: `member_manager.py` and `validation.py` are imported by the application but were not included in this review — they're expected to expose `add_member`, `list_members`, `search_members` and the `required` / `positive_int` helpers respectively, matching the calls used in `main.py` and `book_manager.py`.

## Requirements

- Python 3.7+
- No external dependencies (uses the built-in `sqlite3` module)

## Configuration

Settings live in `config.py`:

| Setting | Default | Description |

| `DB_PATH` | `library.db` (in the project directory) | SQLite database file location |
| `LOAN_DAYS` | `14` | Number of days a book may be borrowed before it's due |
| `FINE_PER_DAY` | `5.0` | Fine charged per day overdue (in ₹) |

## Installation

1. Clone or download the project files into a single directory.
2. Ensure all modules (`main.py`, `config.py`, `database.py`, `validation.py`, `book_manager.py`, `member_manager.py`, `issue_return.py`, `reports.py`) are present in the same folder.
3. No `pip install` is required — the project uses only the standard library.

## Usage

Run the application from the project directory:

bash
python main.py


On first run, `initialize_database()` creates `library.db` and the required tables automatically. You'll see a menu:


========== LIBRARY MANAGEMENT SYSTEM ==========
1. Add Book
2. View Books
3. Search Books
4. Add Member
5. View Members
6. Search Members
7. Issue Book
8. Return Book
9. Active Loans
10. Transaction History
11. Dashboard Report
12. Overdue Report
0. Exit
===============================================


Enter the number corresponding to the action you want to perform and follow the prompts.

### Menu Guide

| Option | Action |

|1| Add a book — prompts for ISBN, Title, Author, Category, Total copies 
| 2 | View all books, sorted by title 
| 3 | Search books by keyword (matches title, author, ISBN, or category) 
| 4 | Add a member — prompts for Member code, Name, Email, Phone 
| 5 | View all registered members 
| 6 | Search members by keyword 
| 7 | Issue a book — prompts for Book ID and Member ID 
| 8 | Return a book — prompts for Transaction ID, prints the calculated fine 
| 9 | View currently active (unreturned) loans 
| 10 | View full transaction history (most recent first) 
| 11 | View a dashboard summary (books, members, available copies, issued/returned counts, total fines) 
| 12 | View overdue loans and how many days each is overdue 
| 0 | Exit the application 

## Data Model

The SQLite database (`library.db`) has three tables:

`books`
- `id`, `isbn` (unique), `title`, `author`, `category`
- `total_copies`, `available_copies` (both must be non-negative; `total_copies > 0`)
- `created_at` (timestamp)

`members`
- `id`, `member_code` (unique), `name`, `email` (unique), `phone`
- `created_at` (timestamp)

`transactions`
- `id`, `book_id` (FK → books), `member_id` (FK → members)
- `issue_date`, `due_date`, `return_date`
- `fine`, `status` (`ISSUED` or `RETURNED`)

## Business Rules

- A book can only be issued if `available_copies > 0`; issuing decrements `available_copies` by 1, and returning increments it back.
- The due date is set to `issue_date + LOAN_DAYS` (14 days by default).
- On return, any days past the due date are multiplied by `FINE_PER_DAY` (₹5/day by default) to compute the fine.
- A book cannot be deleted while it has an active (`ISSUED`) transaction.
- Updating a book's total copies cannot reduce them below the number currently borrowed.

## Error Handling

Invalid input (e.g., non-numeric IDs, missing required fields) and database constraint violations (e.g., duplicate ISBNs or emails) raise `ValueError` or `sqlite3.IntegrityError`, which `main.py` catches and displays as a friendly error message without crashing the application.

## License

This project is provided as-is for educational and personal use.

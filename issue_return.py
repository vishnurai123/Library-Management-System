"""Book issue and return operations."""
from datetime import date, timedelta
from database import get_connection
from config import LOAN_DAYS, FINE_PER_DAY

def issue_book(book_id, member_id):
    today = date.today()
    due = today + timedelta(days=LOAN_DAYS)
    with get_connection() as conn:
        book = conn.execute("SELECT available_copies FROM books WHERE id=?", (book_id,)).fetchone()
        member = conn.execute("SELECT id FROM members WHERE id=?", (member_id,)).fetchone()
        if not book:
            raise ValueError("Book not found.")
        if not member:
            raise ValueError("Member not found.")
        if book["available_copies"] <= 0:
            raise ValueError("No available copy.")
        conn.execute(
            """INSERT INTO transactions(book_id,member_id,issue_date,due_date,status)
               VALUES(?,?,?,?, 'ISSUED')""",
            (book_id, member_id, today.isoformat(), due.isoformat())
        )
        conn.execute(
            "UPDATE books SET available_copies=available_copies-1 WHERE id=?", (book_id,)
        )

def return_book(transaction_id):
    today = date.today()
    with get_connection() as conn:
        tx = conn.execute(
            "SELECT * FROM transactions WHERE id=? AND status='ISSUED'", (transaction_id,)
        ).fetchone()
        if not tx:
            raise ValueError("Active transaction not found.")
        due = date.fromisoformat(tx["due_date"])
        overdue_days = max(0, (today - due).days)
        fine = overdue_days * FINE_PER_DAY
        conn.execute(
            "UPDATE transactions SET return_date=?, fine=?, status='RETURNED' WHERE id=?",
            (today.isoformat(), fine, transaction_id)
        )
        conn.execute(
            "UPDATE books SET available_copies=available_copies+1 WHERE id=?", (tx["book_id"],)
        )
        return fine

def active_transactions():
    with get_connection() as conn:
        return conn.execute("""
            SELECT t.id, b.title, m.name, t.issue_date, t.due_date
            FROM transactions t
            JOIN books b ON b.id=t.book_id
            JOIN members m ON m.id=t.member_id
            WHERE t.status='ISSUED'
            ORDER BY t.due_date
        """).fetchall()

def transaction_history():
    with get_connection() as conn:
        return conn.execute("""
            SELECT t.*, b.title, m.name
            FROM transactions t
            JOIN books b ON b.id=t.book_id
            JOIN members m ON m.id=t.member_id
            ORDER BY t.id DESC
        """).fetchall()

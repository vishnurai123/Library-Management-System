"""Reporting and analytics functions."""
from database import get_connection

def dashboard():
    with get_connection() as conn:
        return {
            "books": conn.execute("SELECT COUNT(*) c FROM books").fetchone()["c"],
            "members": conn.execute("SELECT COUNT(*) c FROM members").fetchone()["c"],
            "available_copies": conn.execute("SELECT COALESCE(SUM(available_copies),0) c FROM books").fetchone()["c"],
            "issued": conn.execute("SELECT COUNT(*) c FROM transactions WHERE status='ISSUED'").fetchone()["c"],
            "returned": conn.execute("SELECT COUNT(*) c FROM transactions WHERE status='RETURNED'").fetchone()["c"],
            "fine": conn.execute("SELECT COALESCE(SUM(fine),0) c FROM transactions").fetchone()["c"],
        }

def overdue_transactions():
    from datetime import date
    with get_connection() as conn:
        return conn.execute("""
            SELECT t.id, b.title, m.name, t.due_date,
                   CAST(julianday(?) - julianday(t.due_date) AS INTEGER) AS overdue_days
            FROM transactions t
            JOIN books b ON b.id=t.book_id
            JOIN members m ON m.id=t.member_id
            WHERE t.status='ISSUED' AND date(t.due_date) < date(?)
            ORDER BY t.due_date
        """, (date.today().isoformat(), date.today().isoformat())).fetchall()

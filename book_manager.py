"""CRUD operations for books."""
from database import get_connection
from validation import required, positive_int

def add_book(isbn, title, author, category, total_copies):
    isbn = required(isbn, "ISBN")
    title = required(title, "Title")
    author = required(author, "Author")
    category = required(category, "Category")
    total_copies = positive_int(total_copies, "Total copies")
    with get_connection() as conn:
        conn.execute(
            """INSERT INTO books(isbn,title,author,category,total_copies,available_copies)
               VALUES(?,?,?,?,?,?)""",
            (isbn, title, author, category, total_copies, total_copies)
        )

def list_books():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM books ORDER BY title").fetchall()

def search_books(keyword):
    keyword = f"%{required(keyword, 'Search keyword')}%"
    with get_connection() as conn:
        return conn.execute(
            """SELECT * FROM books
               WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ? OR category LIKE ?
               ORDER BY title""",
            (keyword, keyword, keyword, keyword)
        ).fetchall()

def update_book(book_id, isbn, title, author, category, total_copies):
    total_copies = positive_int(total_copies, "Total copies")
    with get_connection() as conn:
        row = conn.execute("SELECT total_copies, available_copies FROM books WHERE id=?", (book_id,)).fetchone()
        if not row:
            raise ValueError("Book not found.")
        borrowed = row["total_copies"] - row["available_copies"]
        if total_copies < borrowed:
            raise ValueError(f"Total copies cannot be less than borrowed copies ({borrowed}).")
        available = total_copies - borrowed
        conn.execute(
            """UPDATE books SET isbn=?, title=?, author=?, category=?,
               total_copies=?, available_copies=? WHERE id=?""",
            (required(isbn,"ISBN"), required(title,"Title"), required(author,"Author"),
             required(category,"Category"), total_copies, available, book_id)
        )

def delete_book(book_id):
    with get_connection() as conn:
        active = conn.execute(
            "SELECT COUNT(*) AS c FROM transactions WHERE book_id=? AND status='ISSUED'", (book_id,)
        ).fetchone()["c"]
        if active:
            raise ValueError("Cannot delete a book while it is issued.")
        try:
            conn.execute("DELETE FROM books WHERE id=?", (book_id,))
        except Exception as e:
            raise ValueError("Book could not be deleted.") from e

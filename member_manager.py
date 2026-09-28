"""CRUD operations for library members."""
from database import get_connection
from validation import required, email

def add_member(member_code, name, member_email, phone):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO members(member_code,name,email,phone) VALUES(?,?,?,?)",
            (required(member_code,"Member code"), required(name,"Name"),
             email(member_email), required(phone,"Phone"))
        )

def list_members():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM members ORDER BY name").fetchall()

def search_members(keyword):
    keyword = f"%{required(keyword, 'Search keyword')}%"
    with get_connection() as conn:
        return conn.execute(
            """SELECT * FROM members
               WHERE name LIKE ? OR member_code LIKE ? OR email LIKE ? OR phone LIKE ?
               ORDER BY name""",
            (keyword, keyword, keyword, keyword)
        ).fetchall()

def update_member(member_id, member_code, name, member_email, phone):
    with get_connection() as conn:
        if not conn.execute("SELECT 1 FROM members WHERE id=?", (member_id,)).fetchone():
            raise ValueError("Member not found.")
        conn.execute(
            "UPDATE members SET member_code=?, name=?, email=?, phone=? WHERE id=?",
            (required(member_code,"Member code"), required(name,"Name"),
             email(member_email), required(phone,"Phone"), member_id)
        )

def delete_member(member_id):
    with get_connection() as conn:
        active = conn.execute(
            "SELECT COUNT(*) AS c FROM transactions WHERE member_id=? AND status='ISSUED'", (member_id,)
        ).fetchone()["c"]
        if active:
            raise ValueError("Cannot delete a member with issued books.")
        conn.execute("DELETE FROM members WHERE id=?", (member_id,))

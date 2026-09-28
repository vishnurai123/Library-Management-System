"""Console application entry point for Library Management System."""
import sqlite3
from database import initialize_database
import book_manager as books
import member_manager as members
import issue_return as lending
import reports

def show_rows(rows):
    if not rows:
        print("\nNo records found.")
        return
    for row in rows:
        print(dict(row))

def menu():
    initialize_database()
    while True:
        print("""
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
""")
        choice = input("Enter choice: ").strip()
        try:
            if choice == "1":
                books.add_book(input("ISBN: "), input("Title: "), input("Author: "),
                               input("Category: "), input("Total copies: "))
                print("Book added successfully.")
            elif choice == "2":
                show_rows(books.list_books())
            elif choice == "3":
                show_rows(books.search_books(input("Keyword: ")))
            elif choice == "4":
                members.add_member(input("Member code: "), input("Name: "),
                                   input("Email: "), input("Phone: "))
                print("Member.member_code added successfully.")
            elif choice == "5":
                show_rows(members.list_members())
            elif choice == "6":
                show_rows(members.search_members(input("Keyword: ")))
            elif choice == "7":
                lending.issue_book(int(input("Book ID: ")), int(input("Member ID: ")))
                print("Book issued successfully.")
            elif choice == "8":
                fine = lending.return_book(int(input("Transaction ID: ")))
                print(f"Book returned. Fine: ₹{fine:.2f}")
            elif choice == "9":
                show_rows(lending.active_transactions())
            elif choice == "10":
                show_rows(lending.transaction_history())
            elif choice == "11":
                print(reports.dashboard())
            elif choice == "12":
                show_rows(reports.overdue_transactions())
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        except (ValueError, sqlite3.IntegrityError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    menu()

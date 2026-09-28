# Project Diagrams

## 1. System Architecture

```text
+---------------------+
|      Librarian      |
+----------+----------+
           |
           v
+---------------------+
|   main.py / CLI     |
+----------+----------+
           |
           v
+---------------------------------------------+
| Book | Member | Issue/Return | Reports     |
+----------------------+----------------------+
                       |
                       v
              +----------------+
              |   SQLite DB    |
              +----------------+
                       |
          +------------+------------+
          | books | members | txns  |
          +-------------------------+
```

## 2. Workflow

```text
START
  |
Initialize Database
  |
Display Menu
  |
Select Operation
  |
Validate Input
  |
Process Request
  |
Read/Update Database
  |
Display Result
  |
Return to Menu ---- No ----> Exit
  |
 Yes
  |
Menu
```

## 3. Use Case Diagram

```text
             +-----------------------------+
             | Library Management System   |
             |                             |
Librarian -->| Manage Books                |
Librarian -->| Manage Members              |
Librarian -->| Issue Book                  |
Librarian -->| Return Book                 |
Librarian -->| Search Records              |
Librarian -->| View Reports               |
             +-----------------------------+
```

## 4. Class/Component Diagram

```text
+----------------+
| Database       |
| get_connection |
| initialize     |
+-------+--------+
        |
        +------------------+
        |                  |
+-------v--------+ +-------v---------+
| Book Manager   | | Member Manager  |
| add/list/...   | | add/list/...    |
+-------+--------+ +-------+---------+
        |                  |
        +--------+---------+
                 |
          +------v-------+
          | IssueReturn  |
          | issue/return |
          +------+-------+
                 |
          +------v-------+
          | Reports      |
          +--------------+
```

## 5. Sequence Diagram - Issue Book

```text
Librarian -> main.py: Select Issue Book
main.py -> issue_return.py: issue_book(book_id, member_id)
issue_return.py -> Database: Check book
issue_return.py -> Database: Check member
issue_return.py -> Database: Insert transaction
issue_return.py -> Database: Decrease available copies
Database --> issue_return.py: Success
issue_return.py --> main.py: Success
main.py --> Librarian: Display confirmation
```

## 6. ER Diagram

```text
+----------------+       +---------------------+       +----------------+
| BOOKS          |       | TRANSACTIONS        |       | MEMBERS        |
+----------------+       +---------------------+       +----------------+
| PK id          |<----- | FK book_id          |       | PK id          |
| isbn           |       | FK member_id        | ----->| member_code    |
| title          |       | issue_date          |       | name           |
| author         |       | due_date            |       | email          |
| category       |       | return_date         |       | phone          |
| total_copies   |       | fine                |       +----------------+
| available      |       | status              |
+----------------+       +---------------------+
```

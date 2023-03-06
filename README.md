# Ebookstore

This is a Python program that uses SQLite to create a simple ebookstore database and provides a menu-based interface for adding, updating, deleting, and searching books in the database.

## Requirements
Python 3
SQLite
## Setup
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the following command to create the database: sqlite3 ebookstore.db < schema.sql.
4. Run the program with python bookstore.py.
### Usage
When you run the program, you will be presented with a menu of options:
                **** WELCOME TO THE BOOKSHOP ****

Select an option:
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit
Enter your choice:

### Add a book
To add a book, select option 1 from the main menu and enter the book details as prompted.

### Update a book
To update a book, select option 2 from the main menu and enter the book ID and the new details for the book.

### Delete a book
To delete a book, select option 3 from the main menu and enter the book ID of the book you want to delete.

### Search for books
To search for books, select option 4 from the main menu and enter a keyword to search for. The program will return all books whose title or author contains the keyword.

### Exit the program
To exit the program, select option 0 from the main menu. The program will save any changes made to the database and close the database connection.

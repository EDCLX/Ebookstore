

import sqlite3

# connect to the database
conn = sqlite3.connect('ebookstore.db')

# create the books table if it doesn't exist
conn.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    qty INTEGER
);
''')

# populate the books table
conn.execute('''
INSERT INTO books (id, title, author, qty) VALUES
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3002, 'Harry Potter and the Philosopher''s Stone', 'J.K. Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12);
''')

# define functions for each menu option

def add_book():
    id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = int(input("Enter book quantity: "))
    conn.execute(f"INSERT INTO books (id, title, author, qty) VALUES ({id}, '{title}', '{author}', {qty});")
    conn.commit()
    print("\nBook added successfully.\n")

def update_book():
    id = int(input("Enter book ID: "))
    title = input("Enter new title (leave blank to keep current title): ")
    author = input("Enter new author (leave blank to keep current author): ")
    qty = input("Enter new quantity (leave blank to keep current quantity): ")
    update_fields = []
    if title:
        update_fields.append(f"title = '{title}'")
    if author:
        update_fields.append(f"author = '{author}'")
    if qty:
        update_fields.append(f"qty = {qty}")
    if not update_fields:
        print("\nNo changes specified.\n")
        return
    update_query = f"UPDATE books SET {', '.join(update_fields)} WHERE id = {id}"
    conn.execute(update_query)
    conn.commit()
    print("\nBook updated successfully.\n")

def delete_book():
    id = int(input("Enter book ID: "))
    conn.execute(f"DELETE FROM books WHERE id = {id}")
    conn.commit()
    print("\nBook deleted successfully.\n")

def search_books():
    keyword = input("Enter search keyword: ")
    search_query = f"SELECT * FROM books WHERE title LIKE '%{keyword}%' OR author LIKE '%{keyword}%'"
    results = conn.execute(search_query).fetchall()
    if not results:
        print("\nNo books found.\n")
        return
    print("\nSearch results:")
    for result in results:
        print(result)

# main program loop
while True:
    print("\t\t\t**** WELCOME TO THE BOOKSHOP ****")
    print("\nSelect an option:")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        search_books()
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")

# close the database connection
conn.close()

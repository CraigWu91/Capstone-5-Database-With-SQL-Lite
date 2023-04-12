# Import SQL Lite module
# Create database connection
# Create cursor object
import sqlite3
db = sqlite3.connect('ebookstore')
cursor = db.cursor()

# Create table 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)
''')
db.commit()

# Create entries
cursor = db.cursor()
id1 = 3001
title1 = "A Tale of Two Cities"
author1 = "Charles Dickens"
qty1 = 30

id2 = 3002
title2 = "Harry Potter and the Philosopher's Stone"
author2 = "J.K. Rowling"
qty2 = 40

id3 = 3003
title3 = "The Lion, the Witch and the Wardrobe"
author3 = "C. S. Lewis"
qty3 = 25

id4 = 3004
title4 = "The Lord of the Rings"
author4 = "J.R.R Tolkien"
qty4 = 37

id5 = 3005
title5 = "Alice in Wonderland"
author5 = "Lewis Carroll"
qty5 = 12

# Insert book 1
cursor.execute('''INSERT INTO books(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id1, title1, author1, qty1))
print('First book inserted')

# Insert book 2
cursor.execute('''INSERT INTO books(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id2, title2, author2, qty2))
print('Second book inserted')

# Insert book 3
cursor.execute('''INSERT INTO books(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id3, title3, author3, qty3))
print('Third book inserted')

# Insert book 4
cursor.execute('''INSERT INTO books(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id4, title4, author4, qty4))
print('Fourth book inserted')

# Insert book 5
cursor.execute('''INSERT INTO books(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id5, title5, author5, qty5))
print('Fifth book inserted')

db.commit()

# Function to add a new entry
def enter_book():
    db = sqlite3.connect('ebookstore')
    cursor = db.cursor()
    cursor.execute('SELECT MAX(id) FROM books')
    max_id = cursor.fetchone()[0]
    id = max_id + 1 if max_id else 1
    while True:
        try:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            qty = int(input("Enter the quantity of the book: "))
            cursor.execute('''INSERT INTO books (id, title, author, qty) VALUES (?, ?, ?, ?)''', (id, title, author, qty))
            print("Book added successfully")
            break
        except ValueError:
            print("Incorrect data type, please try again")
    db.commit()
    db.close()

# Function to update an existing entry
def update_book():
    db = sqlite3.connect('ebookstore')
    cursor = db.cursor()
    while True:
        try:
            book_id = int(input("Enter the ID of the book you want to update: "))
            cursor.execute('''SELECT * FROM books WHERE id = ?''', (book_id,))
            book = cursor.fetchone()
            if book:
                print(f"Current book information: ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")
                title = input("Enter the new title of the book : ")
                author = input("Enter the new author of the book : ")
                qty = int(input("Enter the new quantity of the book : "))
                if title:
                    cursor.execute('''UPDATE books SET title = ? WHERE id = ?''', (title, book_id))
                if author:
                    cursor.execute('''UPDATE books SET author = ? WHERE id = ?''', (author, book_id))
                if qty:
                    cursor.execute('''UPDATE books SET qty = ? WHERE id = ?''', (qty, book_id))
                print("Book updated successfully")
                break
            else:
                print("Book not found")
        except ValueError:
            print("Incorrect ID or data type, please try again")
    db.commit()
    db.close()

# Function to delete an entry
def delete_book():
    db = sqlite3.connect('ebookstore')
    cursor = db.cursor()
    while True:
        try:
            book_id = int(input('''Enter the ID of the book you want to delete: '''))
            cursor.execute('''SELECT * FROM books WHERE id = ?''', (book_id,))
            cursor.fetchone()
            cursor.execute('''DELETE FROM books WHERE id = ?''', (book_id,))
            print("Book deleted successfully.")
            break
        except:
            print("Incorrect ID or data type, please try again")
    db.commit()
    db.close()

# Function to search and print an entry
def search_books():
    db = sqlite3.connect('ebookstore')
    cursor = db.cursor()
    search = input("Enter the title or author of the book: ")
    cursor.execute('''SELECT * FROM books WHERE title LIKE ? OR author LIKE ?''', (search, search))
    books = cursor.fetchall()
    if books:
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")
    else:
        print("No results found.")
    db.close()

# Logic for the menu
# Drop table when exit so code can run again from the beginning
while True:
    menu = input('''
        1) Enter book
        2) Update book
        3) Delete book
        4) Search books
        0) Exit\n\n''')
    if menu == "1":
        enter_book()
    if menu == "2":
        update_book()
    if menu == "3":
        delete_book()
    if menu == "4":
        search_books()
    if menu == "0":
        cursor.execute('''DROP TABLE books''')
        exit()
    else:
        print("Please select appropriate menu option")

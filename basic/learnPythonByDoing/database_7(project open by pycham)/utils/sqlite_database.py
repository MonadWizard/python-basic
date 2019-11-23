import sqlite3

"""
we make database which is sqlite
Concerned with storing and retrieving books from a sql 
"""


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS books(name text primary key , author text, read integer)')  # name can't be
    # dublicate, cause name primary key. we don't need id, cause we don't connect this table to other

    connection.commit()
    connection.close()


def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    # cursor.execute(f"INSERT INTO books VALUES('{name}', '{author}', 0)")    #need to make fString, but that's not
    # safe. you can fetch sequleInjection attack
    cursor.execute(f"INSERT INTO books VALUES(?, ?, 0)", (name, author))

    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    # books = cursor.fetchall()     # fetchall give a tuple as [(name, author, read), (name,author,read)] now we
    # convert tuple to dictionary to work same as before.
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in
             cursor.fetchall()]  # listcomprehention can convert tuple to needed dictionary.

    connection.close()

    return books


def mark_book_as_read(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE books SET read=1 where name=?', (name,))

    connection.commit()
    connection.close()


def delete_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE name=?', (name,))

    connection.commit()
    connection.close()

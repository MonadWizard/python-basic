import json
import os

"""
we make database which is sqlite
Concerned with storing and retrieving books from a json
[
    {
    'name': 'bookName'
    'author': 'bookAuthorName'
    'read': True
    }
    {
    'name': 'bookName2'
    'author': 'bookAuthorName2'
    'read': False
    }
]
"""


books_file = 'books.json'


def create_book_table():
    with open(books_file, 'a') as file:
        if os.stat(books_file).st_size == 0:   # check if .json file is empty
            json.dump([], file)  # empty file isn't valid json so we declar an empty list
        else:
            pass


def add_book(name,author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _update_save_all_books(books)


def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def _update_save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if name == book['name']:
            book['read'] = True
    _update_save_all_books(books)   #for rewrite update read and save it permanently




def delete_book(name):
    books = get_all_books()

    # for book in books:
    #     if name == book['name']:
    #         books.remove(book)
                      #  or we can work same using list comprehention

    books = [book for book in books if book['name'] != name]  # put all books on new list which arn't match

    _update_save_all_books(books)   #for rewrite update read and save it permanently









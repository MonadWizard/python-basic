"""
we make database which is sqlite

Concerned with storing and retrieving books from a list. which change to csv file to save data permanently on next files
"""
books = []



def add_book(name,author):
    books.append({'name': name, 'author': author, 'read': False})


def get_all_books():
    return books


def mark_book_as_read(name):
    for book in books:
        if name == book['name']:
            book['read'] = True


def delete_book(name):
    for book in books:
        if name == book['name']:
            books.remove(book)

            #  or we can work same using list comprehention
    # global books
    # books = [book for book in books if book['name'] != name]









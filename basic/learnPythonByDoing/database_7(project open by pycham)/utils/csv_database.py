"""
we make database which is sqlite

Concerned with storing and retrieving books from a list. which change to csv file to save data permanently on next files
"""
books_file = 'books.txt'


def create_book_table():
    with open(books_file, 'a'):
        pass          # just make it to present books.txt file


def add_book(name,author):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},0\n')


def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]    # strip use for ignor /n    readlines() for read all line

    return [    #[[name,author,0],[name,author,0]]
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if name == book['name']:
            book['read'] = '1'
    _update_save_all_books(books)   #for rewrite update read and save it permanently


def _update_save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(name):
    books = get_all_books()

    for book in books:
        if name == book['name']:
            books.remove(book)
                      #  or we can work same using list comprehention
            # books = [book for book in books if book['name'] != name]  # put all books on new list which arn't match

    _update_save_all_books(books)   #for rewrite update read and save it permanently









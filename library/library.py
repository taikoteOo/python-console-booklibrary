from . import Book


class Library:
    id_ = 0
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if isinstance(book, Book):
            Library.id_ += 1
            self.books[Library.id_] = book

    def get_book_info(self, book_id):
        return self.books.get(book_id)

    def get_books(self):
        return self.books

    def search_book(self, query):
        results = {}
        for id_, book in self.books.items():
            if query.lower() in book.autor.lower():
                results[id_] = book
        return results

    def book_delete(self, id_):
        if id_.isdigit():
            if int(id_) in self.books:
                return self.books.pop(int(id_))
        raise ValueError('Неверный или некорректный id')

    @classmethod
    def get_book_count(cls):
        return cls.id_
from . import Book


class Library:
    def __init__(self, storage):
        self.storage = storage
        self.books = storage
        self.last_id = None

    def _get_last_id_book(self):
        last_id = self.storage.get_last_id()
        return last_id

    def increment_book_id(self):
        self.last_id = int(self._get_last_id_book())
        self.last_id += 1
        self.storage.increment_last_id()

    def add_book(self, book):
        if isinstance(book, Book):
            self.increment_book_id()
            book.id = str(self.last_id)
            self.storage.write_data(book.to_dict())
            return book
        raise ValueError('Неверный формат книги!')

    def get_book_by_id(self, book_id):
        book = self.books.get(book_id)
        if book:
            return book
        raise ValueError('Такой книги нет')

    def get_book_by_isbn(self, isbn):
        for id_, book in self.books.items():
            if isbn == book.get('isbn'):
                return id_, book
        raise ValueError('Такой книги нет')

    def get_books(self):
        books = self.storage.read_data()
        return books

    def get_books_by_author(self, author):
        books = {}
        for id_, book in self.books.items():
            if author.lower() in book.author.lower():
                books[id_] = book
        return books

    def get_books_by_title(self, title):
        books = {}
        for id_, book in self.books.items():
            if title.lower() in book.title.lower():
                books[id_] = book
        return books

    def search_book(self, query):
        """
        Поиск по названию или автору. Во избежание повторений результатов,
        если книга нашлась по автору, то по названию уже поиска не будет.
        :param query: Строка и искомым названием или автором
        :return: Словарь с найденными книгами
        """
        results = {}
        for id_, book in self.books.items():
            if query.lower() in book.author.lower():
                results[id_] = book
            elif query.lower() in book.title.lower():
                results[id_] = book
        return results

    def get_books_from_years(self, start_year, end_year):
        """
        Поиск по промежутку лет.
        Учитывает порядок ввода и возвращает ошибку, если первый год больше второго.
        Возвращает ошибку, если введены не числа.
        :param start_year: Год начала поиска
        :param end_year: Год окончания поиска
        :return: Словарь с найденными книгами
        """
        if start_year.isdigit() and end_year.isdigit():
            if start_year < end_year:
                start = int(start_year)
                end = int(end_year)
                results = {}
                for id_, book in self.books.items():
                    if  start <= book.year <= end:
                        results[id_] = book
                return results
            raise ValueError('Первый год должен быть меньше второго')
        raise ValueError('Года должны быть числами!')

    def book_delete(self, id_):
        if id_.isdigit():
            if int(id_) in self.books:
                return self.books.pop(int(id_))
        raise ValueError('Неверный или некорректный id')

    def get_book_count(self):
        pass
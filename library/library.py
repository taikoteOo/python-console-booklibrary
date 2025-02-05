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
        """
        Поиск по названию или автору. Во избежание повторений результатов,
        если книга нашлась по автору, то по названию уже поиска не будет.
        :param query: Строка и искомым названием или автором
        :return: Словарь с найденными книгами
        """
        results = {}
        for id_, book in self.books.items():
            if query.lower() in book.autor.lower():
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

    @classmethod
    def get_book_count(cls):
        return cls.id_
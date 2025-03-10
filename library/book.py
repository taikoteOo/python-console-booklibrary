import uuid
from datetime import datetime
from core.enums import GENRES


class Book:
    def __init__(self, title, author, year, genre):
        """
        Конструктор класса Book
        :param title: Название книги
        :param autor: Автор книги
        :param year: ГОд издания
        :param genre: Жанр книги (по умолчанию None)
        :param isbn: ISBN книги (по умолчанию None)
        """
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.__isbn = uuid.uuid4().hex[:9]
        self.id = None

    def get_info(self):
        """
        Возвращает строку с информацией о книге
        :return: Строка с информацией о книге
        """
        info = f'{self.title} - {self.author} ({self._year})'
        if self.genre:
            info += f', Жанр: {self.genre}'
        info += f', ISBN: {self.__isbn}'

        return info

    @staticmethod
    def is_valid_year(year):
        if isinstance(year, int):
            if 1445 < year <= datetime.today().year:
                return True
            else:
                return False
        elif isinstance(year, str):
            if year.isdigit():
                if 1445 < int(year) <= datetime.today().year:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def is_older_than(self, year):
        """
        Проверяет, была ли книга издана до указанного года
        :param year: Год издания
        :return: bool
        """
        if self.is_valid_year(year):
            return self._year < year
        else:
            raise ValueError('Неверное значение для года издания')

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year):
        if self.is_valid_year(new_year):
            self._year = new_year
        else:
            raise ValueError('Неверное значение для года издания')

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if genre.lower() in GENRES:
            self._genre = genre
        else:
            raise ValueError('Неизвестный жанр')

    def get_book_age(self):
        current_year = datetime.today().year
        return current_year - self._year

    def to_dict(self):
        data = {
            'id': self.id,
            'author': self.author,
            'title': self.author,
            'year': self.year,
            'genre': self.genre,
            'ISBN': self.__isbn
        }
        return data

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn

    @classmethod
    def from_dict(cls, book_data):
        book = Book(
            author =book_data['author'],
            title=book_data['title'],
            year=book_data['year'],
            genre=book_data['genre'],
        )
        book.isbn = book_data['ISBN']
        book.id = book_data['id']
        return book
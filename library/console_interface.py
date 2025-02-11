import sys
from . import Book


class ConsoleInterface:
    def __init__(self, source):
        self.library = source

    def main_menu(self):
        print('Добро пожаловать в ИС "Электронная библиотека"')
        print('Выберете нужное действие')
        print('1. Показать все книги')
        print('2. Добавить книгу')
        print('3. Поиск книг')
        print('4. Удалить книгу')
        print('0. Выйти')
        self.process_main_menu()

    def process_main_menu(self):
        action = input('>>> ')
        match action: #Условие, вроде если
            case '1':
                self.show_books()
            case '2':
                self.add_book()
            case '3':
                self.search_book()
            case '4':
                self.delite_book()
            case '0':
                sys.exit()
            case _:
                print('Выберете нужный пункт меню')

    def show_books(self):
        books = self.library.get_books()
        for book in books:
            print(book.get_info())
        self.footer_menu()

    def add_book(self):
        author = input('Введите автора: ')
        title = input('Введите название: ')
        year = input('Введите год: ')
        genre = input('Введите жанр: ')
        try:
            book = Book(author=author, title=title, year=year, genre=genre)
            self.library.add_book(book)
            print('Книга успешно добавлена')
        except ValueError as err:
            print(err)
            self.add_book()
        self.footer_menu()


    def search_book(self):
        print('Поиск книги')
        self.footer_menu()

    def delite_book(self):
        print('Удаление книги')
        self.footer_menu()

    def footer_menu(self):
        print('Введите 1 для возврата в главное меню')
        print('Введите 0 для выхода из программа')
        action = input('>>> ')
        match action:
            case '1':
                self.main_menu()
            case '0':
                sys.exit()
            case _:
                print('Выберете необходимое действие')
                self.footer_menu()
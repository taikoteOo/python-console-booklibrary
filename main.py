from library import Book, Library, ConsoleInterface


def main():
    library = Library()
    console = ConsoleInterface()

    console.main_menu()
    console.process_main_menu()


    # book_1 = Book(title='Капитанская дочка', autor='А.С.Пушкин', year=1836, genre='Роман')
    # book_2 = Book(title='Герой нашего времени', autor='М.Ю.Лермонтов', year=1836, genre='Роман')
    #
    # library.add_book(book_1)
    # library.add_book(book_2)
    #
    # books = library.get_books()
    # for id_, book in books.items():
    #     print(f'{id_}.{book.get_info()}')
    # print(library.get_book_count())
    #
    # query = 'пуш'
    # results = library.search_book(query)
    # if results:
    #     print('Найденные книги:')
    #     for id_, book in results.items():
    #         print(f'{id_}.{book.get_info()}')
    # else:
    #     print('Ничего не найдено')
    #
    # id_for_del = '1'
    # book_delete = library.book_delete(id_for_del)
    # print(f'Удалена книга id = {book_delete.get_info()}')
    #
    # # books = library.get_books()
    # for id_, book in books.items():
    #     print(f'{id_}.{book.get_info()}')


if __name__ == '__main__':
    main()
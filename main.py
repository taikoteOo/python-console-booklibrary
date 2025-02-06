from library import Book, Library, ConsoleInterface
from db import CSVStorage


def main():
    csv_storage = CSVStorage('book.csv')
    library = Library(storage = csv_storage)
    console = ConsoleInterface(source=library)

    while True:
        console.main_menu()



    # book_1 = Book(title='Капитанская дочка', autor='А.С.Пушкин', year=1836, genre='Роман')
    # book_2 = Book(title='Герой нашего времени', autor='М.Ю.Лермонтов', year=1839, genre='Роман')
    # book_3 = Book(title='Граф Монте-Кристо', autor='Александра Дюма', year=1846, genre='Роман')
    # book_4 = Book(title='Александра Дюма', autor='Александра Дюма', year=1846, genre='Роман')
    #
    # library.add_book(book_1)
    # library.add_book(book_2)
    # library.add_book(book_3)
    # library.add_book(book_4)

    # books = library.get_books()
    # for id_, book in books.items():
    #     print(f'{id_}.{book.get_info()}')
    # print(library.get_book_count())
    #
    # query = 'дю'
    # results = library.search_book(query)
    # if results:
    #     print('Найденные книги:')
    #     for id_, book in results.items():
    #         print(f'{id_}.{book.get_info()}')
    # else:
    #     print('Ничего не найдено')

    # start = '1812'
    # end = '1850'
    # results = library.get_books_from_years(start, end)
    # if results:
    #     print('Найденные книги:')
    #     for id_, book in results.items():
    #         print(f'{id_}.{book.get_info()}')
    # else:
    #     print('Ничего не найдено')
    # #
    # id_for_del = '1'
    # book_delete = library.book_delete(id_for_del)
    # print(f'Удалена книга id = {book_delete.get_info()}')
    #
    # # books = library.get_books()
    # for id_, book in books.items():
    #     print(f'{id_}.{book.get_info()}')



if __name__ == '__main__':
    main()
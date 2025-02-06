import csv
import os


class CSVStorage:
    def __init__(self, filename):
        file_exist = os.path.isfile(filename)
        self.file = open(filename, 'a+', encoding='utf-8')
        fields = ['author', 'title', 'year', 'genre', 'ISBN']
        writer = csv.DictWriter(self.file, fieldnames=fields)  # Создаёт объект, который можно перевести в словарь, принимает файл и имена полей
        if not file_exist:
            writer.writeheader() # Метод, который записывает заголовки


    def write_data(self, book):
        writer = csv.DictWriter(self.file, fieldnames=book.keys())
        writer.writerow(book)


    def read_data(self):
        pass
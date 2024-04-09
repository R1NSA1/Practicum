import csv

def save_table_csv(file_name, data):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in data:
            csv_writer.writerow(row)                # записываются в файл file_name


def load_table_csv(file_name):
    with open(file_name) as f:
        reader = csv.reader(f)
        file = list(reader)
        for i in file:
            print(*i)

# load_table('test.csv')

# save_table([
#     ['Имя', 'Возраст', 'Город'],
#     ['Анна', 25, 'Москва'],
#     ['Иван', 30, 'Санкт-Петербург'],
#     ['Ольга', 28, 'Новосибирск']
# ]
# )

def save_table_txt(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as f:
        for row in data:
            f.write('\t'.join([str(i) for i in row]) + '\n')


def print_table_txt(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            print(i, end='')


print_table_txt('dw.txt')

def get_rows_by_number(table_name: str, start: int, stop: int, copy_table=False):
    with open(table_name, 'r', encoding='utf-8') as f:
        table = f.readlines()
        table_new = []
        for i in range(start, stop + 1):
            table_new.append(table[i - 1])

    if copy_table:
        with open(f'{table_name}_copy', 'w', encoding='utf-8') as f:
            for row in table_new:
                f.write(''.join([str(i) for i in row]))

    else:
        with open(table_name, 'w', encoding='utf-8') as f:
            for row in table_new:
                f.write(''.join([str(i) for i in row]))


get_rows_by_number('dw.csv', 1,2,1)


def set_values()


print(set_values('dw.txt', column='Возраст'))

import re
from random import randint


def file_handler(file):
    with open(file, 'tw', encoding='utf-8') as f:
        print(file)

    lst_num = [randint(1, 20) for _ in range(randint(1, 20))]
    lst_str = [f'str_{i}' for i in range(randint(1, 20))]
    lst = list(zip(lst_num, lst_str))

    with open(file, 'w') as f:
        for i in lst:
            f.write(f'{i[0]} {i[1]}\n')

    print_file(file)


def print_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        str_data = f.read()
        str_data = str_data.replace(str(randint(1, 20)), 'example')
        print(str_data)
        print(f'Первое вхождение строки example - {str_data.find("example")}')
        str_example_all = [m.start() for m in re.finditer("example", str_data)]
        print(f'Все вхождения строки example - {str_example_all}')
        str_data = re.sub(r'example', r'elpmaxe', str_data)
        print(f'Найденные строки заменены на новые: \n{str_data}')
        print(re.findall(r'\b\w +\b', str_data))


file_handler('test.txt')

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
        for line in f:
            print(line)


file_handler('test.txt')

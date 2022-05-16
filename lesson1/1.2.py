import os


def print_directory_contents(path: str):
    files = os.listdir(path)
    print(files)
    for i in files:
        if not os.path.isfile(f'{path}\{i}'):
            print(f'{path}\{i}:', end=' ')
            print_directory_contents(f'{path}\{i}')


print_directory_contents('C:\Program Files')

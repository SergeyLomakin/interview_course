import os
import re


def get_filename(name):
    regex = r"(.+\\)*(.+)\."
    file_path = os.path.abspath(name)
    result = re.findall(regex, file_path)
    print(f'Имя файла: {result[0][1]}')
    print(f'Путь до файла: {file_path}')


get_filename('python.exe')

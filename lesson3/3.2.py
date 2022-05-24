try:
    num = input('Введите число: ').split('.')
    if len(num) > 2:
        raise ValueError
    if len(num) == 1 and num[0].isdigit():
        print('Введенное число целое')
        exit(0)
    print(num[0] == num[1])
except IndexError:
    print('Это не число')
except ValueError:
    print('Должна быть одна точка')

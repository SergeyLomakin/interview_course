from random import randint

list_key = [f'k{i}' for i in range(randint(1, 10))]
list_value = [f'v{i}' for i in range(randint(1, 10))]

dir_list = {}

v = len(list_value)
for k in range(len(list_key)):
    if k < v:
        dir_list[list_key[k]] = list_value[k]
        continue
    dir_list[list_key[k]] = None

print(f'keys: {list_key}')
print(f'values: {list_value}')
print(dir_list)

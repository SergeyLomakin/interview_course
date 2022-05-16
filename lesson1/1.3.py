import random


def random_number(begin: int, end: int):
    results = {}

    for i in range(25):
        results[f'elem_{i}'] = random.randint(begin, end)

    return results


print(random_number(0, 5))

def bank_deposit(cash, term: int, replenishment=0):
    user_rate = 0

    rates = (
        {'begin_sum': 1000, 'end_sum': 10000, '6': 5, '12': 6, '24': 5},
        {'begin_sum': 10000, 'end_sum': 100000, '6': 6, '12': 7, '24': 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, '6': 7, '12': 8, '24': 7.5},
    )

    for i in rates:
        if i['begin_sum'] <= cash < i['end_sum']:
            user_rate = i[str(term)]

    for i in range(term):
        if i == 0 or i == term-1:
            cash += round(cash * (user_rate / 1200), 2)
        else:
            cash += round(cash * (user_rate / 1200) + replenishment, 2)

    return f'Сумма вклада на конец срока: {cash}'


print(bank_deposit(10000, 6, 1000))

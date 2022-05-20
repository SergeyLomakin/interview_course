class ItemDiscount:
    def __init__(self, name, price):
        self._name = name
        self._price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self._name} {self._price}'


ex = ItemDiscountReport('board', 100)
print(ex.get_parent_data())

ex.price = 120
print(ex.get_parent_data())

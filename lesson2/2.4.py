class ItemDiscount:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def change_price(self, price):
        self._price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        return f'{self._name} {self._price * ((100 - self.discount) / 100)}'

    def get_parent_data(self):
        return f'{self._name} {self._price}'


ex = ItemDiscountReport('board', 100, 10)
print(ex)

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


class ItemDiscountReportName(ItemDiscountReport):
    def get_info(self):
        return f'name: {self._name}'


class ItemDiscountReportPrice(ItemDiscountReport):
    def get_info(self):
        return f'price: {self._price}'


ex1 = ItemDiscountReportName('board', 100)
print(ex1.get_info())
ex2 = ItemDiscountReportPrice('board', 100)
print(ex2.get_info())

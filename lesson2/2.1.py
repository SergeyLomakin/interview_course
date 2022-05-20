class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self.name} {self.price}'


ex = ItemDiscountReport('board', 100)
print(ex.get_parent_data())

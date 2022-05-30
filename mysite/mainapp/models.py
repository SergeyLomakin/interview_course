from django.db import models


class Product(models.Model):
    category = models.name = models.CharField('имя', max_length=16, default=None)
    name = models.CharField('имя', max_length=64)
    add_date = models.DateTimeField('время', auto_now_add=True)
    price = models.DecimalField('цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField('количество на складе', default=0)

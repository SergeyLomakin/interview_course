from django.shortcuts import render

from .models import Product


def index(request):
    all_products = Product.objects.all()
    context = {
        'title': 'Главная',
        'all_products': all_products
    }
    return render(request, 'index.html', context)

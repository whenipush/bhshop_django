from django.shortcuts import render
from .models import Store

# Create your views here.



def catalog_page(requests):
    product = Store.objects.all()

    context = {
        'product': product,
    }
    return render(requests, 'catalog/catalog.html', context=context)


def cart_page(requests):
    product = Store.objects.all()

    context = {
        'product': product,
    }
    return render(requests, 'cart/cart.html', context=context)
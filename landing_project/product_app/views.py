from django.shortcuts import render, get_object_or_404

from .models import Product, Advantage


def index(request):
    list_products = Product.objects.all()
    context = {
        'list_products': list_products,
    }
    return render(request, 'index.html', context)


def product(request, id_product):
    product = get_object_or_404(Product, id=id_product)
    list_advantages = Advantage.objects.filter()
    context = {
        'product': product,
        'list_advantages': list_advantages,
    }
    return render(request, 'detail.html', context)


def create_order(request, id):

    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
        }
    return render(request, 'create_order.html', context)



    
    
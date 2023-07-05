from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import Product, Order


def index(request):
    list_products = Product.objects.all()
    context = {
        'list_products': list_products,
    }
    return render(request, 'landing/index.html', context)


def product(request, id):
    product = get_object_or_404(Product, id=id)
    list_advantages = Product.objects.get(id=id).advantages.all()
    context = {
        'product': product,
        'list_advantages': list_advantages,
    }
    return render(request, 'landing/detail.html', context)


def create_order(request, id):
    order = Order()
    
    if request.method == 'POST':
        order.customer = request.POST.get('customer')
        order.product = Product.objects.get(id=id)
        order.save()
        return HttpResponseRedirect(f'/order_complete/{id}')
    else:
        product = Product.objects.get(id=id)
        context = {
            'order': order,
            'product': product,
        }
        return render(request, 'landing/create_order.html', context)


def order_complete(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product,
    }
    return render(request, 'landing/order_complete.html', context)
    
from django.shortcuts import render

from .models import Product, Advantage


def index(request):
    list_products = Product.objects.all()
    list_advantages = Advantage.objects.all()
    context = {
        'list_products': list_products,
        'list_advantages': list_advantages,
    }
    return render(request, 'index.html', context)




    
    
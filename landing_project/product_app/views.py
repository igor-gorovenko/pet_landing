from django.shortcuts import render, get_object_or_404

from .models import Product, Advantage
from .forms import ProductCreateForm


def index(request):
    list_products = Product.objects.all()
    list_advantages = Advantage.objects.all()
    context = {
        'list_products': list_products,
        'list_advantages': list_advantages,
    }
    return render(request, 'index.html', context)


def create_order(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
        }
    return render(request, 'create_order.html', context)



    
    
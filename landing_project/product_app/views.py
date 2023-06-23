from django.shortcuts import get_object_or_404, render, HttpResponse
from django.template import loader

from .models import Product, Advantage


def index(request):
    list_products = Product.objects.all()
    list_advantages = Advantage.objects.all()
    context = {
        'list_products': list_products,
        'list_advantages': list_advantages,
    }
    return render(request, 'index.html', context)


def form(request):
    template = loader.get_template('form.html')
    return HttpResponse(template.render())

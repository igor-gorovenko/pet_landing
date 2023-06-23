from django.shortcuts import render, HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

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


# class SignUp(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = "registration/signup.html"

    
    
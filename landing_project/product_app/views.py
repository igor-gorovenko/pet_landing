from django.shortcuts import render, HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def form(request):
    template = loader.get_template('form.html')
    return HttpResponse(template.render())

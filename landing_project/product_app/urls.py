from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create_order/<int:id>', views.create_order, name='create_order')
]
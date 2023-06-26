from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_product>/', views.product, name='product'),
    path('create_order/<int:id>', views.create_order, name='create_order'),
    path('order_complete/<int:id_product>', views.order_complete, name='order_complete'),
]

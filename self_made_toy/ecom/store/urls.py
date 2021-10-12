from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('index', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('<int:id>', views.detail, name='detail'),
    path('add/<int:id>', views.show, name='show'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('increase/<int:id>', views.increase, name='increase'),
    path('decrease/<int:id>', views.decrease, name='decrease'),
]

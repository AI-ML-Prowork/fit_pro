from django.urls import path
from .views import *

app_name = 'admin_panel'

urlpatterns = [
    path('', base, name='base'),
    path('dashboard', dashboard, name='dashboard'),
    path('add_product', add_product, name='add_product'),
    path('product_list', product_list, name='product_list'),

]

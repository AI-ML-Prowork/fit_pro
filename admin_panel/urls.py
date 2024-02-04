from django.urls import path
from .views import *

app_name = "admin_panel"

urlpatterns = [
    path('admin_base', base, name='base'),
    path('add_product', add_product, name='add_product'),
    path('product_list', product_list, name='product_list'),

]

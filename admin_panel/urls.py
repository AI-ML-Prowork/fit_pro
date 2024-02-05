from django.urls import path
from .views import *

app_name = 'admin_panel'

urlpatterns = [
    path('', base, name='base'),
    path('index', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('add_product', add_product, name='add_product'),
    path('product_list', product_list, name='product_list'),
    path('all_user_rewards', all_user_rewards, name='all_user_rewards'),
    path('all_user_profiles', all_user_profiles, name='all_user_profiles'),

]

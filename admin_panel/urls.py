from django.urls import path
from .views import *

app_name = 'admin_panel'

urlpatterns = [
    # path('', base, name='base'),
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('add_product', add_product, name='add_product'),
    path('product_list', product_list, name='product_list'),
    path('all_user_rewards', all_user_rewards, name='all_user_rewards'),
    path('all_user_profiles', all_user_profiles, name='all_user_profiles'),


    #API CALLS 
    path("product_list_api", product_list_api, name='product_list_api'),
    path("add_product_api", add_product_api, name='add_product_api'),

    # path("user_list_api", user_list_api, name='user_list_api'),
    # path("add_user_api", add_user_api, name='add_user_api'),

    # path("profile_list_api", profile_list_api, name='profile_list_api'),
    # path("add_profile_api", add_profile_api, name='add_profile_api'),

    # path("order_list_api", order_list_api, name='order_list_api'),
    # path("add_order_api", add_order_api, name='add_order_api'),

    # path("wallet_list_api", wallet_list_api, name='wallet_list_api'),
    # path("add_money_to_wallet", add_money_to_wallet, name='add_money_to_wallet'),
]

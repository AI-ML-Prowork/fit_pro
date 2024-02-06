from django.urls import path
from .views import *

app_name = "user_panel"

urlpatterns = [
    # __________ NEW REQUIREMENTS_________#
    path('fitness_hra', fitness_hra, name='fitness_hra'),


    #______________________________________#
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout, name='logout'),
    
    path('', base, name='base'),
    
    path('add_user_profile', add_user_profile, name='add_user_profile'),

    path('add_reward', add_reward, name='add_reward'),
    path('reward_history', reward_history, name='reward_history'),
    
    path('add_wallet_transaction', add_wallet_transaction, name='add_wallet_transaction'),
    path('wallet_history', wallet_history, name='wallet_history'),
    
    path('add_order', add_order, name='add_order'),
    path('orders_history', orders_history, name='orders_history'),



#______________API VIEW__________________

    path("add_profile_api", add_profile_api, name='add_profile_api'),

    path("add_money_to_wallet", add_money_to_wallet, name='add_money_to_wallet'),

    path("user_list_api", user_list_api, name='user_list_api'),
    path("add_user_api", add_user_api, name='add_user_api'),
    
    path("order/", orders_api.as_view(), name='order'),
    path("reward/", rewards_api.as_view(), name='reward'),

]

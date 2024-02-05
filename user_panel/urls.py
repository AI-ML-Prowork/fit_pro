from django.urls import path
from .views import *

app_name = "user_panel"

urlpatterns = [

    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    # path('logout/', logout, name='logout'),
    
    path('', home, name='home'),
    
    path('add_user_profile', add_user_profile, name='add_user_profile'),

    path('add_reward', add_reward, name='add_reward'),
    path('reward_history', reward_history, name='reward_history'),
    
    path('add_wallet_transaction', add_wallet_transaction, name='add_wallet_transaction'),
    path('wallet_history', wallet_history, name='wallet_history'),
    
    path('add_order', add_order, name='add_order'),
    path('orders_history', orders_history, name='orders_history'),



#______________API VIEW__________________
    path("order/", orders_api.as_view(), name='order'),
    path("reward/", rewards_api.as_view(), name='reward'),

]

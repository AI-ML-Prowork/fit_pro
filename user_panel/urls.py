from django.urls import path
from .views import *

app_name = "user_panel"

urlpatterns = [
    # User Panel Homepage
    path('', home, name='home'),
    path('add_user_profile', add_user_profile, name='add_user_profile'),
    path('add_reward', add_reward, name='add_reward'),
    path('reward_history', reward_history, name='reward_history'),
    path('add_wallet_transaction', add_wallet_transaction, name='add_wallet_transaction'),
    

]

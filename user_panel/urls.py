from django.urls import path
from .views import *

app_name = "user_panel"

urlpatterns = [
    # User Panel Homepage
    path('', base, name='base'),
    

]

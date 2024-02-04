from django.contrib import admin

# Register your models here.
from user_panel.models import UserProfile
class profiling(admin.ModelAdmin):
    list_display = ('user_name', 'age', 'height', 'weight', 'any_disease', 'allergies')

admin.site.register(UserProfile, profiling)


from user_panel.models import Add_reward

class reward(admin.ModelAdmin):
    list_display = ('username', 'steps_count', 'calories_burn', 'rewards', 'last_login', 'registration_date_time', 'age')

admin.site.register(Add_reward, reward)



from user_panel.models import Wallet

class wallet(admin.ModelAdmin):
    list_display = ('amount', 'payment_mode', 'date')

admin.site.register(Wallet, wallet)
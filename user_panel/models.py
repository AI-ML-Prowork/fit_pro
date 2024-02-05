from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user_name = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    any_disease = models.CharField(max_length=100, blank=True, null=True)
    allergies = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user_name
    

class Add_reward(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    steps_count = models.PositiveIntegerField()
    calories_burn = models.PositiveIntegerField()
    rewards = models.CharField(max_length=255)
    last_login = models.DateTimeField(null=True, blank=True)
    registration_date_time = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.username}'s Rewards"
    

class Wallet(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode_choices = [
        ('debit_card', 'Debit Card'),
        ('credit_card', 'Credit Card'),
        ('upi', 'UPI'),
    ]
    payment_mode = models.CharField(max_length=20, choices=payment_mode_choices)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Amount: {self.amount} - Payment Mode: {self.get_payment_mode_display()} - Date: {self.date}"
    


import uuid # ----for unique id generation

class Add_Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    item_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    steps_count = models.PositiveIntegerField()
    calories_burn = models.PositiveIntegerField()
    rewards = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.item_name} - {self.user.username}" 
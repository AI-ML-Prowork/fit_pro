# Generated by Django 5.0.1 on 2024-02-04 17:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_panel", "0002_add_reward"),
    ]

    operations = [
        migrations.CreateModel(
            name="Wallet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "payment_mode",
                    models.CharField(
                        choices=[
                            ("debit_card", "Debit Card"),
                            ("credit_card", "Credit Card"),
                            ("upi", "UPI"),
                        ],
                        max_length=20,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

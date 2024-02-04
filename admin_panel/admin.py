from django.contrib import admin

from admin_panel.models import Add_Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description', 'price', 'quantity', 'size', 'colour', 'material', 'suitable_for', 'pattern']

admin.site.register(Add_Product, ProductAdmin)
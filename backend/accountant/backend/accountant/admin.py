from django.contrib import admin
from .models import Client, Supplier

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'tax_number']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'tax_number']

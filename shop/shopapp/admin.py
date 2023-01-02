from django.contrib import admin
from .models import Book, Order, OrderItem


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    search_fields = ['name']
    fields = ['name', 'price', 'quantity', 'id_in_store', 'image']


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'status']
    search_fields = ['user', 'delivery_adress']
    list_filter = ['status']
    fields = ['user', 'delivery_adress', 'status']
    inlines = [
        OrderItemInline,
    ]








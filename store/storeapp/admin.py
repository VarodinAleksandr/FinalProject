from django.contrib import admin
from .models import Book, BookItem, Order, OrderItem


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
    fields = ['name', 'price']


@admin.register(BookItem)
class BookItemAdmin(admin.ModelAdmin):
    list_display = ['book']
    fields = ['book']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order']
    fields = ['order', 'book_store_id', 'quantity', 'book_item']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['order']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user_email', 'delivery_adress', 'status']
    search_fields = ['user_email', 'delivery_adress']
    fields = ['user_email', 'delivery_adress', 'status', 'order_id_in_shop']
    list_filter = ['status']
    inlines = [
        OrderItemInline,
    ]


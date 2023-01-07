from .models import Order, OrderItem
from rest_framework import serializers


class OrderItemSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField(read_only=True)

    def get_book(self, obj):
        return obj.book.id_in_store

    class Meta:
        model = OrderItem
        fields = ['id', 'quantity', 'book']


class OrderSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField(read_only=True)
    order_item = OrderItemSerializer(read_only=True, many=True)

    def get_user_email(self, obj):
        return obj.user.email

    class Meta:
        model = Order
        fields = ['id', 'delivery_adress', 'user_email', 'order_item']

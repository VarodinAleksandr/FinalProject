from .models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField(read_only=True)

    def get_quantity(self, obj):
        return obj.book_items.all().count()

    class Meta:
        model = Book
        fields = ['id', 'name', 'price', 'quantity']



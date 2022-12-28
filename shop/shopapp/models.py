from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    quantity = models.IntegerField()
    id_in_store = models.IntegerField()

    def __str__(self):
        return f'book with id {self.id}, title:{self.title}, quantity:{self.quantity}'


class Order(models.Model):
    CARD = 'cart'
    ORDER = 'order'
    SUCCESS = 'success'
    FAIL = 'fail'
    STATUS_CHOICE = [
        (CARD, 'card'),
        (ORDER, 'order'),
        (SUCCESS, 'success'),
        (FAIL, 'fail'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default=CARD)
    delivery_adress = models.TextField()

    def __str__(self):
        return f'order for user {self.user}, with status {self.status}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f'order item for order {self.order.id}'

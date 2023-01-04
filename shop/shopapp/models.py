from django.contrib.auth.models import User
from django.db import models
from cart.cart import Cart


class Book(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    quantity = models.IntegerField()
    id_in_store = models.IntegerField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return f'book with id {self.id}, title:{self.name}, quantity:{self.quantity}'


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
    order = models.ForeignKey(Order, related_name='order_item', on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f'order item for order {self.order.id}'




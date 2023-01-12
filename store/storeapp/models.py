from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()

    def __str__(self):
        return f'book with id {self.id}, title:{self.name}'


class BookItem(models.Model):
    book = models.ForeignKey(Book, related_name='book_items', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'book item {self.book}'


class Order(models.Model):
    IN_WORK = 'in_work'
    SUCCESS = 'success'
    FAIL = 'fail'
    STATUS_CHOICE = [
        (IN_WORK, 'in_work'),
        (SUCCESS, 'success'),
        (FAIL, 'fail'),
    ]
    user_email = models.EmailField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default=IN_WORK)
    delivery_adress = models.CharField(max_length=300)
    order_id_in_shop = models.IntegerField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE, null=True, blank=True)
    book_store_id = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()
    book_item = models.ManyToManyField(BookItem)

    def __str__(self):
        return f'order item for order {self.order.id} quantity {self.quantity}'

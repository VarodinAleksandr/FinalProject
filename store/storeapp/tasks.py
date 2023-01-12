import requests
from celery import shared_task

from .models import Order, OrderItem, Book


@shared_task
def sync_orders():
    r = requests.get('http://127.0.0.1:8000/orders/')
    if r.status_code == 200:
        orders = r.json()
        print(orders)
        for i in orders:
            obj, created = Order.objects.update_or_create(
                order_id_in_shop=i['id'],
                defaults={
                    'user_email': i['user_email'], 'delivery_adress': i['delivery_adress'], 'order_id_in_shop': i['id']
                }
            )
            if created:
                for b in i['order_item']:
                    book = Book.objects.get(id=b['book'])
                    OrderItem.objects.create(order_id=obj, book_store_id=book, quantity=b['quantity'])

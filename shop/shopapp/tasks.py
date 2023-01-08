import requests
from celery import shared_task

from .models import Book


@shared_task
def sync_books():
    r = requests.get('http://127.0.0.1:8001/')
    if r.status_code == 200:
        books = r.json()
        for i in books:
            obj, created = Book.objects.update_or_create(
                id_in_store=i['id'],
                defaults={'name': i['name'], 'price': i['price'], 'quantity': i['quantity'], 'id_in_store': i['id']}
            )
    print('Success')
    return True

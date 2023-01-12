import requests
from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail

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


@shared_task
def send_mail_to_user(useremail, order_id):
    print(f'new order with id {order_id} was created')
    superusers = User.objects.filter(is_superuser=True)
    emails = [i.email for i in superusers]
    emails.append(useremail)
    for e in emails:
        send_mail(
            'new order was created',
            f'new order with id {order_id} was created',
            'from@example.com',
            [e],
            fail_silently=True,
        )

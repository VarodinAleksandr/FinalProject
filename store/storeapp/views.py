from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Book
from .serializer import BookSerializer


class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    model = Book

    def get_queryset(self):
        return Book.objects.all()

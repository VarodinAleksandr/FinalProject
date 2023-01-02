from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from django.views import generic

from .models import Book

from .forms import SignUpForm


class BooKListView(generic.ListView):
    model = Book
    template_name = 'shopapp/booklist.html'
    paginate_by = 5


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'shopapp/bookdetail.html'


class LoginView(LoginView):
    template_name = 'shopapp/login.html'

    def get_success_url(self):
        return reverse_lazy('shop:book_list')


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'shopapp/usercreate.html'
    success_url = reverse_lazy('shop:login')











from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from django.views import generic
from rest_framework import generics

from .models import Book, Order, OrderItem

from .forms import SignUpForm, OrderForm

from django.contrib.auth.decorators import login_required
from cart.cart import Cart


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


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(user=request.user, delivery_adress=form.cleaned_data.get('delivery_adress'))
            cart = request.session.get('cart', None)
            for key, value in cart.items():
                book = Book.objects.get(id=value.get('product_id'))
                OrderItem.objects.create(order=order, book=book, quantity=value.get('quantity'))
            cart = Cart(request)
            cart.clear()
            return redirect('shop:book_list')
    if request.method == 'GET':
        form = OrderForm()
        context = {'form': form}
        return render(request, 'shopapp/order.html', context)


@login_required(login_url='/login')
def cart_add(request, id):
    cart = Cart(request)
    product = Book.objects.get(id=id)
    cart.add(product=product)
    return redirect('shop:book_list')


@login_required(login_url='/login')
def item_clear(request, id):
    cart = Cart(request)
    product = Book.objects.get(id=id)
    cart.remove(product)
    return redirect('shop:cart_detail')


@login_required(login_url='/login')
def item_increment(request, id):
    cart = Cart(request)
    product = Book.objects.get(id=id)
    cart.add(product=product)
    return redirect('shop:cart_detail')


@login_required(login_url='/login')
def item_decrement(request, id):
    cart = Cart(request)
    product = Book.objects.get(id=id)
    cart.decrement(product=product)
    return redirect('shop:cart_detail')


@login_required(login_url='/login')
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('shop:cart_detail')


@login_required(login_url='/login')
def cart_detail(request):
    return render(request, 'shopapp/cart_detail.html')


#
# class OrderList(generics.ListAPIView):
#     serializer_class = BookSerializer
#     model = Book
#
#     def get_queryset(self):
#         return Book.objects.all()
#
#
#
#



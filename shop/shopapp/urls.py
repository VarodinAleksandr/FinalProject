from django.urls import path

from .views import (BooKListView, BookDetailView, LoginView, SignUpView, cart_add,
                    item_clear, item_increment, item_decrement, cart_clear, cart_detail, create_order)

app_name = 'shop'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', BooKListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),

    # Cart
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/', cart_detail, name='cart_detail'),
    path('cart/order/', create_order, name='cart_order'),
]

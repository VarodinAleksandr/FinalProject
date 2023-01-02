from django.urls import path

from .views import BooKListView, BookDetailView, LoginView, SignUpView

app_name = 'shop'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', BooKListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
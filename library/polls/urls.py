from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.book_list, name='books'),
    path('users', views.user_list, name='users')
]
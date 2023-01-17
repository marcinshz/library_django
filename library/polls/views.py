from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Book, User
from .serializers import BookSerializer, UserSerializer

def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)

def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
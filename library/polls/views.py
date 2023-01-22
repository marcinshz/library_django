from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework import permissions
from .models import Book, User
from .serializers import BookSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def add_book(self, request, pk=None):
        user = self.get_object()
        book = Book.objects.get(pk=request.data['book_id'])
        user.borrowed_books.add(book)
        return Response({'status': 'book added'})

    @action(detail=True, methods=['post'])
    def remove_book(self, request, pk=None):
        user = self.get_object()
        book = Book.objects.get(pk=request.data['book_id'])
        user.borrowed_books.remove(book)
        return Response({'status': 'book removed'})
    

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
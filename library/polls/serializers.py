from rest_framework import serializers
from .models import Book, User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author']

class UserSerializer(serializers.ModelSerializer):
    borrowed_books = BookSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ['name', 'borrowed_books']

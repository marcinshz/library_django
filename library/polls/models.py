from django.db import models


class Book(models.Model):
    name = models.CharField(max_length = 16)
    author = models.CharField(max_length = 16)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length = 16)
    borrowed_books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name
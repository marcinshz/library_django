from django.db import models


class Book(models.Model):
    name = models.CharField(max_length = 30)
    author = models.CharField(max_length = 30)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length = 30)
    borrowed_books = models.ManyToManyField(Book, null=True, blank=True)
    def __str__(self):
        return self.name
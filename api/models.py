from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name
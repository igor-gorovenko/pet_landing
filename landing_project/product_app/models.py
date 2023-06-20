from django.db import models

class User(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.title
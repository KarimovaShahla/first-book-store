from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=64)
    author_name = models.CharField(max_length=32)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.name}"
from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    page_number = models.IntegerField(default=0)
    genre = models.CharField(max_length=200)
    publish_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
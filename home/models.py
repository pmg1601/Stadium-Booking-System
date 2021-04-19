from django.db import models

# Create your models here.

class Book(models.Model):
    tid = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=50)
    show = models.CharField(max_length=20)
    tier = models.CharField(max_length=10)
    attendees = models.IntegerField()
    date = models.DateField()
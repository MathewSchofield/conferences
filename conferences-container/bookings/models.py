from django.db import models

class Bookings(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    home_church = models.CharField(max_length=200)
    completed = models.BooleanField()
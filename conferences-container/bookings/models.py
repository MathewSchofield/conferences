from django.db import models

class Booking(models.Model):

    #def __str__(self):
    #   return self.email

    email = models.EmailField()
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    home_church = models.CharField(max_length=200)
    completed = models.BooleanField()
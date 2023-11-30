from django.db import models

class Booking(models.Model):

    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    home_church = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)



    #def __str__(self):
    #   return self.email
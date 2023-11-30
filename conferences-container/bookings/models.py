from django.db import models


TITLE_CHOICES = (
    (None, ""),  # By default, no title choice is selected
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms'),
    ('Miss', 'Miss'),
)


class Booking(models.Model):

    title = models.CharField(max_length=4, choices=TITLE_CHOICES, default="")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    home_church = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

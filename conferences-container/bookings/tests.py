from django.test import TestCase
from django.urls import reverse

from .models import Booking

BOOKING_ID = 5

def create_booking():
    return Booking.objects.create(id=BOOKING_ID)


class BookingNewViewTests(TestCase):
    def test_new111(self):
        """ Test the new View. Does not require any parameters. """
        response = self.client.post(reverse("new"))
        self.assertEqual(response.status_code, 200)
        self.assert

    def test_new(self):
        """ Test the new View. Does not require any parameters. """
        response = self.client.get(reverse("new"))
        self.assertEqual(response.status_code, 200)







# ADD MULTIPLE PARAMETERS TO TESTS (add_church, confirm, complete) ######################
class BookingAddChurchViewTests(TestCase):
    """ Test the add_church View. Requires a valid Booking id. """

    def test_invalid_booking_id(self):
        """ Test the add_church view with a booking id that does not exist in the database. """
        response = self.client.get(reverse("add_church", args=[111]))
        self.assertEqual(response.status_code, 404)


    def test_valid_booking_id(self):
        booking = create_booking()
        response = self.client.get(reverse("add_church", args=[BOOKING_ID]))
        self.assertEqual(response.status_code, 200)


# test blank fields

# test missing booking ids e.g. -1

# test that everything works if form is valid
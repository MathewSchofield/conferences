from django.test import TestCase
from django.urls import reverse

from .models import Booking

BOOKING_ID = 5
VIEW_NAMES = ["add_church", "confirm", "complete"]

def create_booking():
    return Booking.objects.create(id=BOOKING_ID)


class BookingNewViewTests(TestCase):
    """ Test the new View. """

    def test_post(self):
        """ Test with a POST request. Does not require any parameters. """
        response = self.client.post(reverse("new"))
        self.assertEqual(response.status_code, 200)


    def test_get(self):
        """ Test with a GET request. Does not require any parameters. """
        response = self.client.get(reverse("new"))
        self.assertEqual(response.status_code, 200)


class BookingViewTests(TestCase):
    """ Test the "add_church", "confirm" and "complete" views. """

    def test_invalid_booking_id(self, view_names = VIEW_NAMES):
        """ Test with a booking id that does not exist in the database. """
        for view_name in view_names:
            response = self.client.get(reverse(view_name, args=[111]))
            self.assertEqual(response.status_code, 404)


    def test_valid_booking_id(self, view_names = VIEW_NAMES):
        booking = create_booking()
        for view_name in view_names:
            response = self.client.get(reverse(view_name, args=[BOOKING_ID]))
            self.assertEqual(response.status_code, 200)


# test blank fields

# test that everything works if form is valid
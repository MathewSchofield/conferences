from django.test import TestCase, RequestFactory
from django.urls import reverse

from .models import Booking

VALID_BOOKING_ID = 5
INVALID_BOOKING_ID = 111
ADD_CHURCH_VIEW_NAME = "add_church"
CONFIRM_VIEW_NAME = "confirm"
COMPLETE_VIEW_NAME = "complete"
#VIEW_NAMES = ["add_church", "confirm", "complete"]

def create_booking():
    return Booking.objects.create(id=VALID_BOOKING_ID)


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


class BookingIdViewTests(TestCase):
    """ Test how the "add_church", "confirm" and "complete" views handle Booking Ids. """


    """ Is this more readable than the commented-out tests below? """
    def response_test(self, view_name, booking_id, response_status):
        response = self.client.get(reverse(view_name, args=[booking_id]))
        self.assertEqual(response.status_code, response_status)

    def test_add_church_invalid_booking_id(self):
        self.response_test(ADD_CHURCH_VIEW_NAME, INVALID_BOOKING_ID, 404)

    def test_add_church_valid_booking_id(self):
        booking = create_booking()
        self.response_test(ADD_CHURCH_VIEW_NAME, VALID_BOOKING_ID, 200)

    def test_confirm_invalid_booking_id(self):
        self.response_test(CONFIRM_VIEW_NAME, INVALID_BOOKING_ID, 404)

    def test_add_church_valid_booking_id(self):
        booking = create_booking()
        self.response_test(CONFIRM_VIEW_NAME, VALID_BOOKING_ID, 200)

    def test_complete_invalid_booking_id(self):
        self.response_test(COMPLETE_VIEW_NAME, INVALID_BOOKING_ID, 404)

    def test_complete_valid_booking_id(self):
        booking = create_booking()
        self.response_test(COMPLETE_VIEW_NAME, VALID_BOOKING_ID, 200)


    """ Is this more readable than the tests above? """
    # def test_invalid_booking_id(self, view_names = VIEW_NAMES):
    #     """ Test with a booking id that does not exist in the database. """
    #     for view_name in view_names:
    #         response = self.client.get(reverse(view_name, args=[111]))
    #         self.assertEqual(response.status_code, 404)


    # def test_valid_booking_id(self, view_names = VIEW_NAMES):
    #     booking = create_booking()
    #     for view_name in view_names:
    #         response = self.client.get(reverse(view_name, args=[VALID_BOOKING_ID]))
    #         self.assertEqual(response.status_code, 200)


class BookingViewRequestTests(TestCase):


    def test_new(self):
        #request = RequestFactory.get("/")
        self.assertEqual(1,1)

# test blank fields

# test that everything works if form is valid

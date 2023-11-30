from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Booking
from .forms import BookingForm, BookingForm2


def index(request):
    return HttpResponse("Hello world!")


def new(request):

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            saved_form = form.save()
            return HttpResponseRedirect(reverse("add_church", args=[saved_form.id]))

    else:
        form = BookingForm()

    return render(request, "new.html", {"form": form})


def add_church(request, booking_id):

    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == "GET":
        form = BookingForm2(instance=booking)

    elif request.method == "POST":
        form = BookingForm2(request.POST, instance=booking)
        if form.is_valid():
            saved_form = form.save()
            return HttpResponseRedirect(reverse("confirm", args=[saved_form.id]))

    return render(request, "bookings/add_church.html", {"form": form})


def confirm(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    return HttpResponse("show all data + confirms. completion flag set to true %s" % booking.first_name)


def complete(request, booking_id):
    return HttpResponse("Completion")

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Booking
from .forms import NewForm


def index(request):
    return HttpResponse("Hello world!")

def new(request):

    if request.method == "POST":
        form = NewForm(request.POST)  # populates the new form with data from request (binding data to form)
        if form.is_valid():
            return HttpResponseRedirect("/")  # test if it goes to the index

    else:
        form = NewForm()

    return render(request, "new.html", {"form": form})

    template = loader.get_template("bookings/new.html")
    return HttpResponse(template.render({}, request))  # No context required

def add_church(request, booking_id):

    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, "bookings/add_church.html", {"booking": booking})



    #return HttpResponse("step 2. for adding church to %s." % booking_id)





def confirm(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    return HttpResponse("show all data + confirms. completion flag set to true %s" % booking.first_name)

def complete(request, booking_id):
    return HttpResponse("Completion")

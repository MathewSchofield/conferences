from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")

def new(request):
    return HttpResponse("new. for putting in details")

def add_church(request, booking_id):
    return HttpResponse("step 2. for adding church to %s." % booking_id)

def confirm(request, booking_id):
    return HttpResponse("show all data + confirms. completion flag set to true")

def complete(request, booking_id):
    return HttpResponse("Completion")

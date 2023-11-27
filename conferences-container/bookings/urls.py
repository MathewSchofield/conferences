from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # e.g. http://localhost:8080/
    path("new/", views.new, name="new"),  # e.g. http://localhost:8080/new/
    path("new/<int:booking_id>/step2/", views.add_church, name="add_church"),
    path("new/<int:booking_id>/confirm/", views.confirm, name="confirm"),
    path("new/<int:booking_id>/complete/", views.complete, name="complete"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("homepage/", views.welcome),
    path("aboutpage/", views.about),
    path("orderpage/", views.order),
    path("bookingpage/", views.booking),
    path("contactpage/", views.contact),
]
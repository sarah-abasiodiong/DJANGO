from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.welcome),
    path("about/", views.about),
    path("order/", views.order),
    path("booking/", views.booking),
    path("contact/", views.contact),
]
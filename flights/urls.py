from django.urls import path
from . import views

# URL Routing: Views are connected to specific URLs via Django's URL routing system.
# In the urls.py file, you map a URL pattern to a specific view.

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book"),
]

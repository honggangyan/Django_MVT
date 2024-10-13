from django.shortcuts import render, get_object_or_404
from flights.models import Flight, Passenger
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404


#  Views are responsible for handling the logic that processes user requests
#  and returns the appropriate responses.
#  Views act as the bridge between the models (which handle the data) and the templates (which handle the presentation).
#  - Handling Requests
#  - Business logic
#  - Types of views: Class-Based Views and Function-Based Views

def index(request):
    return render(request, "flights/index.html", {"flights": Flight.objects.all()})


def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")
    
    return render(
        request,
        "flights/flight.html",
        {
            "flight": flight,
            "passengers": flight.passengers.all(),
            "non_passengers": Passenger.objects.exclude(flights=flight).all(),
        },
    )


def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger_id = int(request.POST["passenger"])
        try:
            passenger = Passenger.objects.get(pk=passenger_id)
            flight.passengers.add(passenger)
            return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
        except Passenger.DoesNotExist:
            return HttpResponseNotFound("Passenger not found")
    else:
        return HttpResponseRedirect(reverse("index"))

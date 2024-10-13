from django.db import models


# Import the models module from Django's database package

# Define the Models and Tables 
class Airport(models.Model):
    # Airport model representing airports in the system
    code = models.CharField(max_length=3)  # Airport code (e.g., JFK, LAX)
    city = models.CharField(max_length=32)  # City where the airport is located

    def __str__(self) -> str:
        # String representation of the Airport object
        return f"{self.city}({self.code})"


class Flight(models.Model):
    # Flight model representing individual flights

    # Origin airport (many flights can have the same origin)
    origin = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="departures"
    )
    # ForeignKey to Airport model, CASCADE deletion
    # 'related_name="departures"' allows accessing all flights departing from an airport
    # via 'airport.departures.all()'

    # Destination airport (many flights can have the same destination)
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="arrivals"
    )
    # ForeignKey to Airport model, CASCADE deletion
    # 'related_name="arrivals"' allows accessing all flights arriving at an airport
    # via 'airport.arrivals.all()'

    # Flight duration in minutes
    duration = models.IntegerField()

    def __str__(self):  # String representation of the Flight
        # Returns a string with flight ID, origin, and destination
        return f"{self.id}: {self.origin} to {self.destination}"

    def is_valid_flight(self):
        # Check if the flight is valid (origin and destination are different)
        return self.origin != self.destination and self.duration > 0
    


class Passenger(models.Model):
    # Passenger model representing individuals who can book flights
    first = models.CharField(max_length=64)  # First name of the passenger
    last = models.CharField(max_length=64)   # Last name of the passenger
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    # Many-to-many relationship with Flight model, can be blank
    # 'related_name="passengers"' allows accessing all passengers of a flight
    # via 'flight.passengers.all()'

    def __str__(self) -> str:
        # String representation of the Passenger object
        return f"{self.first} {self.last}"

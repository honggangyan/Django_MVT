# Airline Management System

This is a Django-based web application for managing airline flights and bookings.

## Features

- User authentication system
- Flight management (add, view, and list flights)
- Passenger management (add passengers to flights)
- Admin interface for managing flights, airports, and passengers

## Project Structure

The project consists of two main Django apps:

1. `flights`: Handles flight-related functionality
2. `users`: Manages user authentication and profiles

## Setup and Installation

1. Clone the repository
2. Install the required dependencies (Django 4.2.15)
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Start the development server: `python manage.py runserver`

## Usage

- Access the admin interface at `/admin/` to manage flights, airports, and passengers
- View the list of flights at `/flights/`
- User authentication is available at `/users/login/` and `/users/logout/`

## Models

- `Airport`: Represents airports with code and city
- `Flight`: Represents flights with origin, destination, and duration
- `Passenger`: Represents passengers with first name, last name, and associated flights

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


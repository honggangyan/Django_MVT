# Airline Management System

A Django-based web application for managing airline flights and bookings.

## Features

- User authentication system
- Flight management (add, view, and list flights)
- Passenger management (add passengers to flights)
- Admin interface for managing flights, airports, and passengers
- Automated testing with Selenium

## Project Structure

The project consists of three main components:

1. `flights`: Handles flight-related functionality
2. `users`: Manages user authentication and profiles
3. `selenium`: Contains automated tests for the application

## Setup and Installation

1. Set up the database:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Create a superuser for admin access:
   ```
   python manage.py createsuperuser
   ```

3. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`
- Admin interface: `http://127.0.0.1:8000/admin/`
- View flights: `http://127.0.0.1:8000/flights/`
- User authentication: `http://127.0.0.1:8000/users/login/` and `http://127.0.0.1:8000/users/logout/`

## Models

- `Airport`: Represents airports with code and city
- `Flight`: Represents flights with origin, destination, and duration
- `Passenger`: Represents passengers with first name, last name, and associated flights

## Testing

### Django Tests

Run Django tests using:
```
python manage.py test
```

### Selenium Tests

To run Selenium tests:
1. Ensure Chrome and ChromeDriver are installed
2. Navigate to the `selenium` directory
3. Run the tests:
   ```
   python tests.py
   ```

## Continuous Integration

This project uses GitHub Actions for CI/CD. The workflow is defined in `.github/workflows/ci.yaml`.


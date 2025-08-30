# Hotel-Management-System

This is a web-based hotel management system built using the Django framework. The system provides an efficient way to manage hotel operations, including room booking, guest management, and staff administration.

# Features
* Room Management: Add, update, and delete rooms with details like room type, price, and availability.
* Guest Management: Register new guests, view guest details, and track their stay history.
* Booking System: Guests can book rooms, view booking history, and cancel reservations.
* Staff Administration: Manage staff accounts and assign roles with different permission levels.
* Dashboard: A comprehensive dashboard to view real-time statistics on room occupancy, revenue, and upcoming bookings.

# Technologies Used
* Backend:

  ** Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.

  ** Python: The core programming language.

# Frontend:

** HTML, CSS, JavaScript: Standard web technologies for building the user interface.

** Bootstrap: A CSS framework for creating responsive and mobile-first websites.

# Database:

** SQLite: The default database in Django, suitable for development. You can configure it to use PostgreSQL or MySQL for production.

# Installation
# Prerequisites
* Python 3.x installed.
* pip (Python package installer).

# Steps
1. Clone the repository:
* git clone https://github.com/your-username/hotel-management-system.git
cd hotel-management-system
2. Create and activate a virtual environment:
* python -m venv venv
  
 #On Windows

 source venv\Scripts\activate

3. Install dependencies:

* pip install -r requirements.txt
4. Run migrations:
* python manage.py makemigrations
* python manage.py migrate
  
5. Create a superuser to access the admin panel:

* python manage.py createsuperuser
6. Run the development server:
* python manage.py runserver
The application will be accessible at http://127.0.0.1:8000.

# Admin Panel
You can access the Django admin panel at http://127.0.0.1:8000/admin. Log in with the superuser credentials you created to manage hotel data.

# Contributing
We welcome contributions! Please feel free to open issues or submit pull requests.

1. Fork the repository.

2. Create your feature branch (git checkout -b feature/AmazingFeature).

3. Commit your changes (git commit -m 'Add some AmazingFeature').

4. Push to the branch (git push origin feature/AmazingFeature).

5. Open a Pull Request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

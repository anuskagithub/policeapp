City Police App
This is a Django-based web application designed to assist the Bangalore City Police Department with efficient data management and capture processes.

Features
-Secure web interface for police operations
-Form handling with validations
-Admin panel for backend data control
-Modular design using Django apps

Tech Stack
-Backend: Python, Django
-Frontend: HTML, CSS (add JS if applicable)
-Database: Default Django ORM (SQLite/MySQL)

Project Structure
Project_App/
└── Scripts/
    └── bangalore_city_police/
        ├── bangalore_city_police/  # Project settings
        ├── capture/                # Django app
        └── manage.py

Getting Started
1. Clone the repository
  git clone https://github.com/anuskagithub/policeapp.git
  cd bangalore-city-police-app

2. Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install dependencies
  pip install -r requirements.txt

4.Run migrations and start server
  python manage.py migrate
  python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.




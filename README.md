City Police App
This is a Django-based web application designed to assist the Bangalore City Police Department with efficient data management and capture processes.
The objective is to develop a web application that captures and stores high-quality facial images and soft biometric information of individuals. The system will include secure user registration and authentication, webcam-based image capture with real-time quality assessment, and a form for collecting personal details. Captured data will be stored in a centralized database with immediate feedback and confirmation upon submission. This application aims to enhance the creation and management of a reliable database for identity verification and security purposes.

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

Flowchart/DFD
<img width="275" alt="image" src="https://github.com/user-attachments/assets/1de218d2-3be4-470a-b800-0e0fa3e83615" />

User Interface
<img width="406" alt="image" src="https://github.com/user-attachments/assets/f47e8a09-27af-4f56-82ea-d0dd09de7621" />
<img width="410" alt="image" src="https://github.com/user-attachments/assets/7c349b17-daca-4dee-884a-f2a6be9823dc" />
<img width="409" alt="image" src="https://github.com/user-attachments/assets/b72eae3d-5a32-4849-8dae-cec8b955bc42" />
<img width="410" alt="image" src="https://github.com/user-attachments/assets/48410e01-8384-4267-ab2a-71afc176199f" />

Admin Interface
<img width="408" alt="image" src="https://github.com/user-attachments/assets/24e8d57a-4ffd-4abd-8250-a88cdf92b5ba" />
<img width="403" alt="image" src="https://github.com/user-attachments/assets/67873230-3acf-421b-ac6c-e47883d7f835" />
<img width="409" alt="image" src="https://github.com/user-attachments/assets/cae97ad2-0e6e-4689-84c3-1bb6d3c7fc6c" />











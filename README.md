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
<img width="229" alt="image" src="https://github.com/user-attachments/assets/52f8d013-3540-43b7-81ca-6c9849549418" />
<img width="276" alt="image" src="https://github.com/user-attachments/assets/dc98ed33-c0e4-4bd3-b634-6fd976eae509" />

<img width="320" alt="image" src="https://github.com/user-attachments/assets/db93f442-3702-4440-97a6-72eb8a4dd106" />
<img width="317" alt="image" src="https://github.com/user-attachments/assets/f499b168-ce1f-4e1c-bbe6-e25bfc0bd4d4" />

Admin Interface
<img width="321" alt="image" src="https://github.com/user-attachments/assets/cae919ee-25b1-45a7-b031-26a9c8a55fae" />
<img width="401" alt="image" src="https://github.com/user-attachments/assets/0180565b-5800-4774-85bf-a2200f4fc5be" />
<img width="407" alt="image" src="https://github.com/user-attachments/assets/e9df182a-46a4-40cd-8ceb-db319353163d" />










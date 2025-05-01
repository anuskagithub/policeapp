### City Police App

<p align='justify' The project involves developing a web application aimed at creating and managing a database of facial images and associated soft biometric information of individuals. This system ensures that high-quality images and accurate data are securely stored and efficiently managed for various applications such as security and identity verification.

The application features user registration and authentication, linking personal information with a unique device ID to restrict access to authorized users only. Users can capture facial images using a webcam, and the system assesses the quality of these images in real-time. A quality bar displays the image quality on a scale from 0% to 100%, with color indicators to signify poor, average, and good quality, ensuring only high-quality images are saved. 

Captured images are temporarily stored, allowing users to review and retake photos if necessary. The application includes a form for entering personal details of the individual, such as name, age, sex, mobile number, and address, creating a comprehensive profile. Upon form submission, the data and high-quality image are securely stored in a centralized database.

The system provides immediate feedback through a confirmation message after successful data submission. This centralized database is designed to be highly secure, protecting sensitive data from unauthorized access. This application is crucial for sectors requiring reliable identification and verification, such as law enforcement and private security, ensuring a dependable and efficient database for future reference.

Features
-Secure web interface for police operations
-Form handling with validations
-Admin panel for backend data control
-Modular design using Django apps

Tech Stack
-Backend: Python, Django
-Frontend: HTML, CSS (add JS if applicable)
-Database: Default Django ORM (SQLite/MySQL) </p>

Project Structure
Project_App/
└── Scripts/
    └── bangalore_city_police/
        ├── bangalore_city_police/  # Project settings
        ├── capture/                # Django app
        └── manage.py

<p align='justify'> align='justify' Getting Started
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

Visit http://127.0.0.1:8000/ in your browser.</p> 

### Flowchart / DFD

<div align="left">
  <img width="275" alt="Flowchart or DFD" src="https://github.com/user-attachments/assets/1de218d2-3be4-470a-b800-0e0fa3e83615" />
</div>

---

### User Interface

<div align="left">
  <img width="406" alt="User Interface 1" src="https://github.com/user-attachments/assets/f47e8a09-27af-4f56-82ea-d0dd09de7621" />
</div>

<div align="left">
  <img width="410" alt="User Interface 2" src="https://github.com/user-attachments/assets/7c349b17-daca-4dee-884a-f2a6be9823dc" />
</div>

<div align="left">
  <img width="409" alt="User Interface 3" src="https://github.com/user-attachments/assets/b72eae3d-5a32-4849-8dae-cec8b955bc42" />
</div>

<div align="left">
  <img width="410" alt="User Interface 4" src="https://github.com/user-attachments/assets/48410e01-8384-4267-ab2a-71afc176199f" />
</div>

---

### Admin Interface

<div align="left">
  <img width="408" alt="Admin Interface 1" src="https://github.com/user-attachments/assets/24e8d57a-4ffd-4abd-8250-a88cdf92b5ba" />
</div>

<div align="left">
  <img width="403" alt="Admin Interface 2" src="https://github.com/user-attachments/assets/67873230-3acf-421b-ac6c-e47883d7f835" />
</div>

<div align="left">
  <img width="409" alt="Admin Interface 3" src="https://github.com/user-attachments/assets/cae97ad2-0e6e-4689-84c3-1bb6d3c7fc6c" />
</div>










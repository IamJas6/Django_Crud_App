# Django CRM Application

This Django CRM Application is designed to manage customer relationships efficiently. It includes user authentication, CRUD operations for records, and a user-friendly interface using Bootstrap themes.

## Table of Contents
- [Basic Setup](#basic-setup)
- [Virtual Environment Setup](#virtual-environment-setup)
- [Django Setup](#django-setup)
- [Project Structure](#project-structure)
- [Features](#features)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)

## Basic Setup

### GitHub Setup
1. Go to your GitHub account.
2. Create a new repository.
3. Open the created repository and copy the link of this repository.

### Visual Studio Code Setup
1. Open VS Code and open any empty folder from your PC.
2. Clone the created repository using the command:
    ```bash
    git clone <copied_link>
    ```
3. Initialize Git:
    ```bash
    git init
    ```

## Virtual Environment Setup
1. Install the virtual environment:
    ```bash
    pip install virtualenv
    ```
2. Create a virtual environment:
    ```bash
    virtualenv venv
    ```
3. Activate the virtual environment:
    ```bash
    venv\scripts\activate
    ```
4. To deactivate the virtual environment:
    ```bash
    deactivate
    ```

## Django Setup
1. Install Django while the virtual environment is activated:
    ```bash
    pip install django
    ```
2. To see the list of installed packages:
    ```bash
    pip list
    ```

### Create Django Project
1. Create a Django project:
    ```bash
    django-admin startproject project_name
    ```
2. Change into your project directory and run the server:
    ```bash
    cd project_name
    python manage.py runserver
    ```

### Create Django App
1. Create a Django app:
    ```bash
    django-admin startapp app_name
    ```
2. Register your app in `settings.py` of the main project folder under `INSTALLED_APPS`:
    ```python
    INSTALLED_APPS = [
        ...
        'app_name',
    ]
    ```
3. Migrate to save your app:
    ```bash
    python manage.py migrate
    ```

### Create Super User for Admin Login
1. Create a super user:
    ```bash
    python manage.py createsuperuser
    ```
2. Provide a username, skip the email, and set a password twice.

## Project Structure
```plaintext
project_name/
│
├── app_name/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   ├── templates/
│   │   ├── app_name/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── project_name/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

## Features
- User Authentication (Register, Login, Logout)
- CRUD Operations for Records
- Admin Dashboard
- Dynamic URLs for Record Management
- Bootstrap Themes for UI

## Usage

### Create and Configure `urls.py` File
1. Create a `urls.py` file in your app and configure the URL.
2. Include app URLs in the main project URL.

### Create Static Folder and Configure in Settings
1. Create a `static` folder inside the main project.
2. Create subfolders `css` and `js`.
3. Configure static files in `settings.py`:
    ```python
    STATICFILES_DIRS = [BASE_DIR / 'static']
    ```

### Create Templates
1. Project-level: Configure templates in project settings under `TEMPLATES -> 'DIRS': [BASE_DIR / 'templates']`.
2. App-level: Create a folder named `templates` inside the app folder and a subfolder with the app name inside `templates`.

### Example Views and Templates
- Simple Views:
    ```python
    from django.shortcuts import render
    from django.http import HttpResponse

    def home(request):
        return render(request, 'crud_app/index.html')
    ```

- Base HTML File:
    ```html
    {% load static %}
    {% block content %}
    <!-- Your content goes here -->
    {% endblock %}
    ```

### Create Forms and Views
1. Create forms in `forms.py`.
2. Render forms in views and handle form submissions.

### CRUD Operations
- Create, Read, Update, and Delete operations for records.

## Screenshots
<!-- Add screenshots here -->

<img src="Screenshot 2024-08-05 151109.png"></img>
<img src="Screenshot 2024-08-05 152253.png"></img>

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

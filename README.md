# Django E-commerce Project - Clothing Store

## Overview

This project is a fully-fledged e-commerce website built using Django. The application allows users to browse, search, and purchase clothing items. The project features user authentication, product management, shopping cart functionality, and order management.

## Features

- User registration and authentication
- Product browsing with search functionality
- Shopping cart and order management
- User profiles with image upload
- Admin panel for product management
- Responsive design

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Clothing
```

### 2. Create and activate virtual environment

```bash
# Create virtual environment
python -m venv myvenv

# Activate virtual environment
# On Windows:
myvenv\Scripts\activate
# On macOS/Linux:
source myvenv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Navigate to project directory

```bash
cd genx
```

### 5. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

## Usage

- Visit `http://127.0.0.1:8000/` in your browser to access the website
- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage products and orders

## Project Structure

```plaintext
Clothing/
├── genx/                      # Main Django project
│   ├── genx/                  # Project settings
│   │   ├── settings.py        # Django settings
│   │   ├── urls.py           # Main URL configuration
│   │   └── wsgi.py           # WSGI application
│   ├── clothing/             # Main app (products, cart, orders)
│   │   ├── models.py         # Database models
│   │   ├── views.py          # View functions
│   │   ├── urls.py           # App URL patterns
│   │   └── templates/        # HTML templates
│   ├── users/                # User management app
│   │   ├── models.py         # User profile models
│   │   ├── views.py          # User-related views
│   │   └── forms.py          # User forms
│   ├── pictures/             # Media files
│   ├── manage.py             # Django management script
│   └── db.sqlite3            # SQLite database
├── requirements.txt          # Python dependencies
└── .gitignore               # Git ignore rules
```

![Screenshot 2024-08-28 161004](https://github.com/user-attachments/assets/8b9408e0-e218-475f-9f10-20413f3ca046)
![Screenshot 2024-08-28 161132](https://github.com/user-attachments/assets/e10e2293-aa6f-4d7a-810e-95f47a7b221c)
![Screenshot 2024-08-28 161055](https://github.com/user-attachments/assets/99f45361-c42b-4bcd-9159-ff72d48f9dd0)
![Screenshot 2024-08-28 161035](https://github.com/user-attachments/assets/64d9a6e7-f453-4592-b467-ecb440d322e9)

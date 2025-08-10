@echo off
REM start.bat - Quick start script for Django Clothing Store

echo 🚀 Starting Django Clothing Store...

REM Activate virtual environment
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else if exist "myvenv\Scripts\activate.bat" (
    call myvenv\Scripts\activate.bat
) else (
    echo ❌ Virtual environment not found. Please run setup.bat first.
    pause
    exit /b 1
)

REM Navigate to Django project
cd genx

REM Start the server
echo 🌐 Starting development server at http://127.0.0.1:8000/
python manage.py runserver

pause

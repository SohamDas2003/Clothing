@echo off
REM setup.bat - Automated setup script for Django Clothing Store (Windows)

echo 🛍️  Setting up Django Clothing Store...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    exit /b 1
)

echo ✅ Python found

REM Create virtual environment if it doesn't exist
if not exist "myvenv" (
    echo 📦 Creating virtual environment...
    python -m venv myvenv
) else (
    echo ✅ Virtual environment already exists
)

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call myvenv\Scripts\activate

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

REM Navigate to Django project
cd genx

REM Run migrations
echo 🗄️  Running database migrations...
python manage.py makemigrations
python manage.py migrate

REM Collect static files (if needed)
echo 📁 Collecting static files...
python manage.py collectstatic --noinput

echo 🎉 Setup complete!
echo.
echo To start the development server:
echo 1. Activate virtual environment: myvenv\Scripts\activate
echo 2. Navigate to project: cd genx
echo 3. Run server: python manage.py runserver
echo.
echo Visit http://127.0.0.1:8000 to view your application

pause

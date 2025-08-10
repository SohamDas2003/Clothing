#!/bin/bash
# setup.sh - Automated setup script for Django Clothing Store

echo "🛍️  Setting up Django Clothing Store..."

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python found"

# Create virtual environment if it doesn't exist
if [ ! -d "myvenv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv myvenv
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source myvenv/Scripts/activate
else
    source myvenv/bin/activate
fi

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Navigate to Django project
cd genx

# Run migrations
echo "🗄️  Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Collect static files (if needed)
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

echo "🎉 Setup complete!"
echo ""
echo "To start the development server:"
echo "1. Activate virtual environment: source myvenv/bin/activate (Linux/Mac) or myvenv\\Scripts\\activate (Windows)"
echo "2. Navigate to project: cd genx"
echo "3. Run server: python manage.py runserver"
echo ""
echo "Visit http://127.0.0.1:8000 to view your application"

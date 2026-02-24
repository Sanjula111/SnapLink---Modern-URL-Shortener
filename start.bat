@echo off
echo 🚀 Starting SnapLink URL Shortener...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
pip install -q -r requirements.txt

REM Create static directory if it doesn't exist
if not exist "static" mkdir static

echo.
echo ✨ SnapLink is starting...
echo 📱 Open http://localhost:5000 in your browser
echo 💡 Press Ctrl+C to stop the server
echo.

REM Run the application
python app.py

pause

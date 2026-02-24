#!/bin/bash

echo "🚀 Starting SnapLink URL Shortener..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

# Create static directory if it doesn't exist
mkdir -p static

echo ""
echo "✨ SnapLink is starting..."
echo "📱 Open http://localhost:5000 in your browser"
echo "💡 Press Ctrl+C to stop the server"
echo ""

# Run the application
python app.py

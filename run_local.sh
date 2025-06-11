#!/bin/bash

# TRAVIA v2.0 - Local Development Script
# =====================================

echo "🚀 Starting TRAVIA v2.0 Local Development Server..."
echo "=============================================="

# Set environment variables for local development
export ENVIRONMENT=development
export PORT=8000
export HOST=0.0.0.0
export LOG_LEVEL=info

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Run the server
echo "🌐 Starting FastAPI server..."
echo "API will be available at: http://localhost:8000"
echo "API Documentation: http://localhost:8000/docs"
echo "Press Ctrl+C to stop the server"
echo "=============================================="

python app.py 
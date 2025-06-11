#!/usr/bin/env python3
"""
TRAVIA v2.0 Production App Entry Point
=====================================

This is the main entry point for the TRAVIA FastAPI application
optimized for production deployment on Zeabur.
"""

import os
import sys
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Import the FastAPI app
from main import app
from config import settings

# Export the app for ASGI servers
__all__ = ["app"]

if __name__ == "__main__":
    import uvicorn
    
    # Run the server
    uvicorn.run(
        "app:app",
        host=settings.host,
        port=settings.port,
        log_level=settings.log_level,
        access_log=True,
        server_header=False,
        date_header=False,
    ) 
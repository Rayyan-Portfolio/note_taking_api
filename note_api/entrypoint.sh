#!/bin/bash

# Apply database migrations
echo "⏳ Running Alembic migrations..."
alembic upgrade head

# Start the FastAPI app
echo "🚀 Starting the FastAPI app..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000

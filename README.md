FastAPI TODO App

This is a simple TODO application built with FastAPI, featuring user authentication and task management functionalities.
Features

    User Authentication
        Register new users
        Authenticate users using JWT tokens

    Task Management
        Create tasks
        View tasks
        Update tasks
        Delete tasks

    Database
        Uses SQLite with SQLAlchemy for data persistence

Installation

    Clone the repository:

    bash

git clone https://github.com/your-username/fastapi-todo-app.git
cd fastapi-todo-app

Install dependencies:

bash

pip install -r requirements.txt

Set up environment variables:

Create a .env file in the root directory with the following variables:

plaintext

SQLALCHEMY_DATABASE_URI="sqlite:///./task.db"
SECRET_KEY="your_secret_key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

Replace "your_secret_key" with a secure random string.

Run the application:

bash

    uvicorn app.main:app --reload

    The API will be available at http://localhost:8000.

API Documentation

    Swagger UI: http://localhost:8000/docs
    ReDoc: http://localhost:8000/redoc

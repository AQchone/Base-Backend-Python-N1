# Base-Backend-Python-N1

## Overview

A Flask-based backend for a product management application with user authentication.

## Features

- RESTful API for product management
- User registration and authentication
- SQLite database integration
- Data validation with Marshmallow
- Comprehensive error handling

## Setup and Installation

### Prerequisites

- Python 3.8+
- pip

### Installation Steps

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python run.py
   ```

## API Endpoints

- `GET /api/products`: List all products
- `POST /api/products`: Create a new product
- `GET /api/products/<id>`: Get product details
- `PUT /api/products/<id>`: Update a product
- `DELETE /api/products/<id>`: Delete a product
- `POST /api/register`: Register a new user
- `POST /api/login`: User login

# SIH_Poseidon

# Indra Project

## Overview

The Indra project is a web application aimed at managing water resources efficiently, with a focus on minimizing non-revenue water. It comprises a Django-based backend for administrative tasks and a React-based frontend for user interaction.

## Prerequisites

- Python 3.x
- Node.js and npm
- PostgreSQL (or any other preferred database)

## Backend (Django)

### Setup

1. Clone this repository.

   
   ```git clone https://github.com/yourusername/indra.git```
   ```cd indra```

2. Create virtual environment

```python -m venv venv```
``source venv/bin/activate``

3. Install Python dependencies.
``` pip install -r requirements.txt```

4. ```python manage.py migrate```

5. ```python manage.py createsuperuser```

6. ```python manage.py runserver```

7. Access the admin panel at http://localhost:8000/admin and log in with your superuser credentials.

# Backend API
### The Django backend provides API endpoints for managing water resources and users. Refer to the API documentation for details.

## Frontend (React)

```cd frontend```
```npm install```
```npm start```

# Frontend UI
### The React frontend offers a user-friendly interface for interacting with the Indra water management system.

Non-Revenue Water (NRW)
Non-revenue water (NRW) refers to water that is lost before it reaches the customer due to leaks, theft, or inaccuracies in measurement. Efficient water resource management is crucial to minimize NRW and ensure sustainable water supply.

Contribution
Feel free to contribute to this project by submitting issues or pull requests. Your contributions are valuable in achieving efficient water resource management.

License
This project is licensed under the MIT License. See the LICENSE file for details.


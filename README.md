# Employee Data Generation & Visualization

A minimal Django + Django REST Framework project to:

- Generate synthetic employee, department, and attendance data
- Store it in PostgreSQL
- Expose REST API endpoints with filtering, pagination, authentication, and throttling
- Self-document the API via Swagger UI
- Render a simple interactive dashboard using Chart.js

## 🛠️ Built With

- Python 3.9+
- Django 4.x
- Django REST Framework
- PostgreSQL
- Faker (for synthetic data)
- drf-yasg (Swagger/OpenAPI)
- Chart.js (frontend visualization)

## 📋 Prerequisites

- Git
- Python 3.9+ (with venv)
- PostgreSQL 12+
- Homebrew (macOS) or your OS's package manager

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/employee-data.git
cd employee-data
```

### 2. Create & activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate.bat     # Windows
```

### 3. Install Python dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Note:** Your requirements.txt should include:
Django, djangorestframework, psycopg2-binary, Faker, drf-yasg, python-dotenv

## 🔧 Configuration

### 4. Configure Your Database

**Option A: Using psql**

Start the psql shell pointing to the default template:

```bash
psql -d template1
```

Run the SQL commands:

```sql
CREATE DATABASE employee_db;
CREATE USER employee_user WITH PASSWORD 'YourStrongP@ssw0rd';
ALTER ROLE employee_user SET client_encoding TO 'utf8';
ALTER ROLE employee_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE employee_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE employee_db TO employee_user;
\q
```

**Option B: Using pgAdmin**

1. Open pgAdmin and connect to your server.
2. Login/Group Roles → Create → New Role:
    - Name: employee_user
    - Password: YourStrongP@ssw0rd
    - Privileges: Can login? checked
3. Databases → Create → New Database:
    - Name: employee_db
    - Owner: employee_user
4. In pgAdmin's Query Tool, run:

```sql
ALTER ROLE employee_user SET client_encoding TO 'utf8';
ALTER ROLE employee_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE employee_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE employee_db TO employee_user;
```

### 5. Update Django Settings

In employee_project/settings.py (or via a .env file):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'employee_db',
        'USER': 'employee_user',
        'PASSWORD': 'YourStrongP@ssw0rd',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS += [
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'employee_app',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '1000/day',
    },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

## 📦 Database Setup & Migrations

### 6. Make Migrations & Migrate

```bash
python manage.py makemigrations
python manage.py migrate
```

## 🔄 Data Generation

### 7. Generate Synthetic Data

A custom management command will create:
- 5 Departments
- 5 Employees
- 25 Attendance Records

```bash
python manage.py generate_data
```

You should see:

```
✅ Synthetic data generated!
```

Verify in the Django shell:

```bash
python manage.py shell
>>> from employee_app.models import Employee, Department, Attendance
>>> Employee.objects.count(), Department.objects.count(), Attendance.objects.count()
```

## 👤 Create a Superuser

### 8. Create an Admin Account

```bash
python manage.py createsuperuser
```

Follow the prompts for username and password.

## ▶️ Running the Project

### 9. Start the Development Server

```bash
python manage.py runserver
```

- API Root: http://127.0.0.1:8000/api/
- Swagger UI: http://127.0.0.1:8000/swagger/
- Django Admin: http://127.0.0.1:8000/admin/
- Dashboard: http://127.0.0.1:8000/dashboard/

## 🌐 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/employees/ | GET, POST | List & create employees (auth required) |
| /api/employees/{id}/ | GET, PUT, DELETE | Retrieve, update, delete a single employee |
| /api/attendance/ | GET | List attendance records |
| /api-auth/login/ | GET, POST | Login for SessionAuthentication |
| /api-auth/logout/ | GET | Logout |
| /swagger/ | GET | Swagger/OpenAPI UI |
| /dashboard/ | GET | Interactive Chart.js dashboard |

## 🔒 Authentication

### Session / Basic Auth
Log in via `/api-auth/login/` and use your session cookie or Basic credentials.

### Token Auth
Generate a token:

```bash
python manage.py drf_create_token <username>
```

Add header in your requests:

```
Authorization: Token <your-token-here>
```

## 📊 Dashboard Visualization

The dashboard template is located at:

```
<project_root>/templates/employee_app/dashboard.html
```

It fetches from `/api/employees/` and renders a bar chart of employee salaries using Chart.js.

## 🚧 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/XYZ`)
3. Commit your changes (`git commit -m "Add feature XYZ"`)
4. Push to the branch (`git push origin feature/XYZ`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See LICENSE for details.
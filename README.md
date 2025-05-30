# ESG Data Management System

A Django REST API backend for managing Environmental, Social, and Governance (ESG) data for companies and their business units.

## Features

- **Company Management**: Add, retrieve, and search companies by name or sector
- **Business Unit Management**: Manage business units within companies
- **ESG Metrics**: Track environmental, social, and governance metrics
- **Metric Values**: Record metric values over time with different reporting periods
- **RESTful APIs**: Full CRUD operations with filtering and search capabilities
- **Service Layer Architecture**: Clean separation of business logic
- **PostgreSQL Integration**: Robust relational database support

## Technology Stack

- **Framework**: Django 5.2.1 with Django REST Framework
- **Database**: PostgreSQL
- **Environment Management**: python-dotenv
- **Architecture**: Service-based layered architecture

## Project Structure

```
esg/
├── esg/                    # Main project directory
│   ├── settings.py         # Django settings with environment variables
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── breathesg/             # Main application directory
│   ├── models.py          # Database models
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # ViewSets for API endpoints
│   ├── services.py        # Business logic layer
│   ├── admin.py           # Django admin configuration
│   └── urls.py            # App URL patterns
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
└── README.md             # This file
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL 12+
- Git

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd esg-data-management
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

Create a PostgreSQL database and user:

```sql
-- Connect to PostgreSQL as superuser
CREATE DATABASE esg_db;
CREATE USER esg_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE esg_db TO esg_user;

-- Connect to esg_db
\c esg_db;
CREATE SCHEMA esg;
GRANT ALL ON SCHEMA esg TO esg_user;
```

### 5. Environment Configuration

```bash
cp .env.example .env
```

Update the `.env` file with your database credentials:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=esg_db
DB_USER=esg_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_SCHEMA=esg
```

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Start Development Server

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

## API Endpoints

### Companies
- `GET /api/companies/` - List all companies
- `POST /api/companies/` - Create a new company
- `GET /api/companies/{id}/` - Retrieve a specific company
- `PUT /api/companies/{id}/` - Update a company
- `DELETE /api/companies/{id}/` - Delete a company
- `GET /api/companies/search/?q=query` - Search companies by name or sector

### Business Units
- `GET /api/business-units/` - List all business units
- `POST /api/business-units/` - Create a new business unit
- `GET /api/business-units/{id}/` - Retrieve a specific business unit
- `PUT /api/business-units/{id}/` - Update a business unit
- `DELETE /api/business-units/{id}/` - Delete a business unit
- `GET /api/business-units/?company=id` - Filter by company

### Metrics
- `GET /api/metrics/` - List all metrics
- `POST /api/metrics/` - Create a new metric
- `GET /api/metrics/{id}/` - Retrieve a specific metric
- `PUT /api/metrics/{id}/` - Update a metric
- `DELETE /api/metrics/{id}/` - Delete a metric
- `GET /api/metrics/?category=E` - Filter by category (E/S/G)

### Metric Values
- `GET /api/metric-values/` - List all metric values
- `POST /api/metric-values/` - Create a new metric value
- `GET /api/metric-values/{id}/` - Retrieve a specific metric value
- `PUT /api/metric-values/{id}/` - Update a metric value
- `DELETE /api/metric-values/{id}/` - Delete a metric value
- `GET /api/metric-values/?business_unit=id` - Filter by business unit
- `GET /api/metric-values/?year=2023` - Filter by year
- `GET /api/metric-values/?category=E` - Filter by metric category

## Data Models

### Company
- `name`: Company name (required)
- `location`: Company location (required)
- `sector`: Business sector (required, choices: Energy, Finance, Tech, Healthcare, Retail)
- `reporting_time`: Reporting period (required)

### Business Unit
- `company`: Foreign key to Company (required)
- `name`: Business unit name (required)
- `location`: Business unit location (required)
- `function`: Business unit function/purpose (required)

### Metric
- `name`: Metric name (required, unique)
- `category`: ESG category (required, choices: E=Environmental, S=Social, G=Governance)
- `description`: Metric description (optional)

### Metric Value
- `business_unit`: Foreign key to Business Unit (required)
- `metric`: Foreign key to Metric (required)
- `reporting_period`: Reporting period (required, e.g., "2023", "Q1 2024")
- `value`: Numeric value (required)
- `unit`: Unit of measurement (required, e.g., "kWh", "%", "incidents")

## Example API Usage

### Create a Company
```bash
curl -X POST http://localhost:8000/api/companies/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Green Energy Corp",
    "location": "New York, USA",
    "sector": "Energy",
    "reporting_time": "Annual 2023"
  }'
```

### Create a Business Unit
```bash
curl -X POST http://localhost:8000/api/business-units/ \
  -H "Content-Type: application/json" \
  -d '{
    "company": 1,
    "name": "Solar Division",
    "location": "California, USA",
    "function": "Solar Panel Manufacturing"
  }'
```

### Create a Metric
```bash
curl -X POST http://localhost:8000/api/metrics/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Energy Consumption",
    "category": "E",
    "description": "Total energy consumed in operations"
  }'
```

### Record a Metric Value
```bash
curl -X POST http://localhost:8000/api/metric-values/ \
  -H "Content-Type: application/json" \
  -d '{
    "business_unit": 1,
    "metric": 1,
    "reporting_period": "2023",
    "value": 15000.5,
    "unit": "kWh"
  }'
```

## Architecture Notes

### Service Layer
The application follows a service-based architecture where:
- **Views**: Handle HTTP requests/responses and input validation
- **Services**: Contain business logic and complex operations
- **Models**: Define data structure and simple database operations

### Key Features Implemented
- ✅ Object-Oriented Programming with Django models
- ✅ PostgreSQL integration with proper schema
- ✅ RESTful API design with Django REST Framework
- ✅ Service-based architecture for clean code separation
- ✅ Environment variable configuration
- ✅ Search functionality for companies
- ✅ Filtering capabilities for metrics and values
- ✅ Proper validation and error handling
- ✅ Database relationships with foreign keys
- ✅ Admin interface for data management

## Testing

You can test the API using:
- Django Admin interface: `http://localhost:8000/admin/`
- DRF Browsable API: `http://localhost:8000/api/`
- Command line tools like `curl` or Postman
- Python requests library

## Future Enhancements

- Add authentication and authorization
- Implement data visualization endpoints
- Add bulk import/export functionality
- Create automated reporting features
- Add metric targets and benchmarking
- Implement audit trails for data changes

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is for educational purposes as part of a Django backend assignment.

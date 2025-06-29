# BrainProt Backend

Welcome to the **BrainProt Backend** – the official API server for BrainProt, built using **Django v4** and the **Django REST Framework**. This backend powers the BrainProt platform, ensuring seamless data management and providing robust API endpoints.

## Features

✅ **Data Management** – Efficient handling of BrainProt's core services.  
✅ **RESTful API Endpoints** – Enabling smooth client-server interactions.  

## Prerequisites

Before setting up the project, ensure you have the following installed:

- [Python 3.8 or higher](https://www.python.org/downloads/) (Recommended Python 3.10)
- [Django v4](https://docs.djangoproject.com/en/4.0/releases/4.0/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/download/)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/brainprot-dev/brainprot-backend.git
   cd brainprot-backend
   ```

2. **Create a Virtual Environment**:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
   
4. **Configure the Database**:

   Create a `.env` file in the root directory with the following template:

   ```env
   DATABASE_NAME=your_database_name
   DATABASE_USER=your_database_user
   DATABASE_PASSWORD=your_database_password
   HOST=localhost
   PORT=5432
   ```

5. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser** (for accessing the Django admin panel):

   ```bash
   python manage.py createsuperuser
   ```

7. **Start the Development Server**:

   ```bash
   python manage.py runserver
   ```

🖥️ Access the server at: `http://127.0.0.1:8000/`

## Project Structure

```
brainprot-backend/
├── BrainProt/                 # Main project directory
│   ├── settings.py            # Project settings
│   ├── urls.py                # URL configurations
│   └── wsgi.py                # WSGI application
├── app_name/                  # General app structure
│   ├── admin.py               # Admin configurations for the app
│   ├── apps.py                # App configuration settings
│   ├── migrations/            # Database migrations
│   ├── models.py              # Database models
│   ├── serializers.py         # DRF serializers
│   ├── views.py               # API views
│   └── urls.py                # App-specific URLs
├── manage.py                  # Django management script
└── requirements.txt           # Python dependencies
```

## API Endpoints

Detailed documentation of the API endpoints is available here: https://www.brainprot.org/api

## Contact

For questions or support, please contact the BrainProt development team at [support@brainprot.org](mailto:support@brainprot.org).

## Citation

Please cite BrainProt Manuscript-

For IBPM (BrainProt v1.0): https://pubs.acs.org/doi/abs/10.1021/acs.jproteome.1c00511
For PhosphoMap (BrainProt v2.0): https://pubmed.ncbi.nlm.nih.gov/36317652/
For BrainProt v3.0: https://www.biorxiv.org/content/10.1101/2023.06.21.545851v1.full

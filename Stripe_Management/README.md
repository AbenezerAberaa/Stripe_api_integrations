# Stripe_Management

This is a Django project called "Stripe_Management" that provides functionalities for managing Stripe payments. It is designed to integrate with the Stripe payment gateway and allows you to perform various tasks related to payment processing.

## Getting Started

To get started with the Stripe_Management project, follow these steps:

### Installation

Clone the repository and navigate to the project directory:

```shell
git clone https://github.com/AbenezerAberaa/Stripe_api_integrations
cd Stripe_Management
```

### Environment Setup

Create and activate a virtual environment:

```shell
python3 -m venv env
source env/bin/activate
```

### Install Dependencies

Install the project dependencies using pip:

```shell
pip install -r requirements.txt
```

### Database Migration

Apply the database migrations:

```shell
python manage.py migrate
```

### Create Superuser

Create a superuser account to access the admin interface:

```shell
python manage.py createsuperuser
```

### Run the Application

Start the development server:

```shell
python manage.py runserver
```

Access the application in your browser at `http://localhost:8000`.

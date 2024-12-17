# Online Shop with Django
This project is an online shop built using Django, following the "Django 5 by Example" tutorial series. The goal of this project is to create a fully functional e-commerce site with product listings, a shopping cart, and user authentication.

## Features
- User registration and Authentication
- Product Listings and Detail Pages
- Shopping Cart Functionality
- Order Management
- Admin Panel for Product Management

## Tech Stack
- Backend: Django 5
- Frontend: HTML, CSS (can be expanded with JavaScript)
- Database: SQLite (or PostgreSQL/MySQL for production)
- Version Control: Git/GitHub for code management

## SetUp Instructions
### Prerequesites
Before running this project, ensure you have Python and pip installed.
1. Clone the repository:
    ```bash
    git clone git@github.com:EmmanuelOnyekachi21/online_shop.git
    ```
2. Navigate into the project folder:
    ```bash
    cd online_shop
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - For Windows
        ```bash
        venv\Scripts\activate
        ```
    - For Linux/macOS:
        ```bash
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Run database migrations:
    ```bash
    python manage.py migrate
    ```
7. Create a superuser (for accessing the Django admin panel):
    ```bash
    python manage.py createsuperuser
    ```
8. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

### Access the App
Go to [localhost](http://127.0.0.1:8000/) to view the online shop.
Go to [localhost-admin](http://127.0.0.1:8000/admin/) to access the admin panel.
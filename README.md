# E-Kart

E-Kart is an e-commerce platform built using Django. This project includes features such as user registration, login, account management, shopping cart, order processing, and a payment system supporting various payment methods including Card, UPI, and Cash on Delivery (COD).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#Features)
- [License](./License)

## Installation

1. Clone the repository:
    ```bash
    https://github.com/anandmohanam/kart.git
    cd e-kart
    ```

2. Create a virtual environment:
    ```bash
    python -m venv env
    ```

3. Activate the virtual environment:
    ```bash
    # On Windows
    .\env\Scripts\activate

    # On macOS/Linux
    source env/bin/activate
    ```

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

1. Access the application at `http://127.0.0.1:8000/`.
2. Register a new user or log in with an existing account.
3. Manage your account, add items to your cart, and proceed to checkout.

## Features

- User registration and authentication
- Account management
- Shopping cart functionality
- Order processing
- Payment system with Card, UPI, and COD options


# Vendor-Management-System-

## Overview

This project is a Django-based API for managing vendors and purchase orders. It provides RESTful endpoints for various operations related to vendor management.

## Setup Instructions

### Prerequisites

Make sure you have the following installed on your system:

- Python (3.x)
- Django
- Django REST Framework
- ...

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/abhinandhhkrishna24/Vendor-Management-System-.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Vendor_Management-System
    ```

3. Create and activate a virtual environment:

    ```bash
    python -m venv vmsenv
    'vmsenv\Scripts\activate'
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

### API Endpoints

#### Vendors

- **List/Create Vendors:** `/api/vendors/` (GET, POST)
- **Retrieve/Update/Delete Vendor:** `/api/vendors/<vendor_id>/` (GET, PUT, DELETE)

#### Purchase Orders

- **List/Create Purchase Orders:** `/api/purchase_orders/` (GET, POST)
  - To retrieve a list of purchase orders or create a new one, use this endpoint.
  - **Query Parameters:**
    - `vendor_id` (optional): Filter purchase orders by vendor ID.

- **Retrieve/Update/Delete Purchase Order:** `/api/purchase_orders/<po_id>/` (GET, PUT, DELETE)
  - To retrieve, update, or delete a specific purchase order, use this endpoint.

#### Vendor Performance

- **Retrieve Vendor Performance Metrics:** `/api/vendors/<vendor_id>/performance/` (GET)

#### Acknowledge Purchase Order

- **Acknowledge a Purchase Order:** `/api/purchase_orders/<po_id>/acknowledge/` (PUT)

### Authentication

Token-based authentication is used to secure API endpoints. To obtain an access token, use the following endpoints:

- **Obtain Access Token:** `/api/token/` (POST)
  - Provide your username and password to obtain an access token.

- **Refresh Access Token:** `/api/token/refresh/` (POST)
  - Use a valid refresh token to obtain a new access token without providing credentials.

Include the obtained access token in the Authorization header for subsequent requests to secure endpoints.

### Testing

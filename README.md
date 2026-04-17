A RESTful API built using FastAPI and PostgreSQL to manage and analyze iPhone sales data for a retail chain.

**Tech Stack**
    Backend Framework: FastAPI
    Database: PostgreSQL
    Database Driver: psycopg2-binary
    Validation: Pydantic
    Server: Uvicorn


**Project Structure**
    dealsource/
    │── app/
    │   ├── main.py        # API routes
    │   ├── db.py          # Database connection
    │   ├── schemas.py     # Pydantic models
    │   ├── crud.py        # Database operations
    │── requirements.txt
    │── README.md



**Setup Instructions**
    1. Clone Repository
    git clone https://github.com/Gaurav7192/dealsource.git
    cd iphone-sales-api
    2. Create Virtual Environment
    python -m venv .venv
    .venv\Scripts\activate   
    3. Install Dependencies
    pip install -r requirements.txt
    


**Database Setup (PostgreSQL)**
    Create Database
    CREATE DATABASE iphone_db;
    Create Table
    CREATE TABLE iphone_sales (
        id SERIAL PRIMARY KEY,
        customer_name VARCHAR(100) NOT NULL,
        phone_model VARCHAR(50) NOT NULL,
        color VARCHAR(30) NOT NULL,
        storage_gb INTEGER NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        sale_date DATE NOT NULL,
        store_location VARCHAR(100) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

**Configure Database Connection**
        Update dealsource/db.py:
        
        psycopg2.connect(
            host="localhost",
            database="iphone_db",
            user="postgres",
            password="your_password"
        )


**Run the Application**
        uvicorn app.main:app --reload
        
        Open in browser:
        
        http://127.0.0.1:8000/docs


**API Endpoints**
    1. Create Sale
    POST /sales
    2. Get All Sales
    GET /sales
    GET /sales?phone_model=iPhone15
    3. Get Sale by ID
    GET /sales/{sale_id}
    4. Update Sale
    PUT /sales/{sale_id}
    5. Delete Sale
    DELETE /sales/{sale_id}
    6. Sales Statistics (Bonus)
    GET /sales/stats

**Sample Request (POST /sales)**

    { "customer_name": "Gaurav", "phone_model": "iPhone15", "color": "Black", "storage_gb": 128, "price": 79999, "sale_date": "2026-04-16", "store_location": "Ahmedabad" }


**Features**
    Full CRUD operations
    Filter sales by phone model
    Sales analytics (total sales, revenue, avg price)
    Clean modular architecture
    PostgreSQL integration




**Assumptions**
    Database and table are created manually
    No authentication implemented (basic API)
    Designed for local development

    
**Future Improvements**
    JWT Authentication
    Docker support
    Environment variables (.env)
    SQLAlchemy ORM integration
    Unit testing
**Author**

Gaurav Singh Bhandari

**Notes**
    This project is built as part of a backend developer assignment to demonstrate:
    
    API design
    Database integration
    Clean code practices

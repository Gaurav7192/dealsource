import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="iphone_db",
        user="postgres",
        password=7192, # this line or page should be git ignore as you create own database passward and user
        cursor_factory=RealDictCursor
    )
# db.py
# MySQL connection functions for SyntaxSafari
# Uses mysql.connector (in CBSE syllabus)

import mysql.connector
def create_connection():
    """Create MySQL connection (change user/password as per your system)."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",                   
            password="koushikee2008", 
            database="syntaxsafari"
        )
        return conn
    except Error as e:
        print("Error while connecting to MySQL:", e)
        return None

def setup_database():
    """Create database and tables if they don't exist."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="koushikee2008"
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS syntaxsafari")
        cursor.close()
        conn.close()
    except Error as e:
        print("Database creation error:", e)

    # Now create tables
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                grade VARCHAR(10),
                language VARCHAR(20)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                result_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                language VARCHAR(20),
                level VARCHAR(15),
                score INT,
                total INT,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
create_connection()
setup_database()

# main.py
# Entry point of SyntaxSafari Project
# Interactive Language Learning App (CBSE Class 12 Project)

import os
from stack_utils import Stack
import db


# ---------- Utility Functions ----------
def teachers(language,grade):
    a=language+"_"+grade+".txt"
    f=open(a,"r")
    b=f.readlines()
    for i in b:
         print(b)
         print("/n")
def welcome_screen():
    print("="*50)
    print(" " * 15 + "Welcome to")
    print(" " * 13 + "✨ SYNTAX SAFARI ✨")
    print("="*50)
    print("\nLearn languages in a fun and simple way!\n")

def get_user_info():
    name = input("Enter your name: ")
    grade = input("Enter your grade: ")
    print("\nAvailable Languages:")
    print("1. French")
    print("2. German")
    print("3. Spanish")
    choice = input("Choose your language (1-3): ")

    if choice == "1":
        language = "French"
    elif choice == "2":
        language = "German"
    elif choice == "3":
        language = "Spanish"
    else:
        language = "French"  # default

    reason = input(f"Why do you want to learn {language}? ")
    teachers(language,grade)
    return name, grade, language, reason

# ---------- Main Program ----------

if __name__ == "__main__":
    # Setup DB on first run
    db.setup_database()

    welcome_screen()
    name, grade, language, reason = get_user_info()

    print("\nThank you,", name)
    print(f"We will help you learn {language} step by step!")
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


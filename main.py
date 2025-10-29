# main.py
# Entry point of SyntaxSafari Project
# Interactive Language Learning App (CBSE Class 12 Project)

import os
from stack_utils import Stack
import db


# ---------- Utility Functions ----------
def test(language,grade):
    for i in range(70):
        print()
    g=language+" "+"test"+"_"+grade+".txt"
    b=open(g,"r")
    k=[]
    v=[]
    score=0
    for i in range(5):
        print("*"*121)
        print(b.readline())
        g=input('ENTER YOUR ANSWER')
        k+=[g+"\n" ]
    for i in range(5):
        a=b.readline()
        v+=[a]
    print("*"*121)
    
    
    print("ANSWER KEY")
    print(k)
    print(v)
    
    for i in range(5):
        print("*"*121)
        c=k[i]
        b=v[i]
        if c.lower()==b.lower():
            print("correct answer")
            score+=5
            print("YOUR ANSWER " ,c)
            print("CORRECT ANSWER",b)
        else:
            print("wrong answer")
            print("YOUR ANSWER " ,c)
            print("CORRECT ANSWER",b)
    print("YOUR SCORE ",score)
    
        
            
        
        
        
     
def teachers(language,grade):
    a=language+"_"+grade+".txt"
    f=open(a,"r")
    b=f.readlines()
    print()
    print()
    for i in b:
         print("*"*121)
         
         print(i)
         time.sleep(2)
         print()
    a=input("DO YOU WISH TO TAKE TEST")
    if a =="y":
        
        test(language,grade)
         
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


    
welcome_screen()
get_user_info()


'''import mysql.connector
def create_connection():
    """Create MySQL connection (change user/password as per your system)."""
    try:
        conn = mysql.connector.connect(
             host="localhost",
             user="root",
              password="Vishnu@12345",
                database="new",
                auth_plugin="mysql_native_password"
            
        )
        return conn
    except Error as e:
        print("Error while connecting to MySQL:", e)
        return None

def setup_database():
    """Create database and tables if they don't exist."""
    
    conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Vishnu@12345",
                database="new",
                auth_plugin="mysql_native_password"
            )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS syntaxsafari")
    cursor.close()
    conn.close()
     
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

setup_database()'''


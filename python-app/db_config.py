import mysql.connector
from mysql.connector import Error
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DB_CONFIG = {
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE"),
    port=int(os.getenv("DB_PORT", 3306))
}

def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        st.error(f"Database connection failed: {e}")
        return None

def create_table():
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        connection.close()

def insert_user(name, age):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        insert_query = "INSERT INTO users (name, age) VALUES (%s, %s)"
        cursor.execute(insert_query, (name, age))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    return False

def get_all_users():
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, age, created_at FROM users ORDER BY created_at DESC")
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return users
    return []
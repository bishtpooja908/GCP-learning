-- Database setup script for Streamlit App
-- Run this script in MySQL to create the database and table

CREATE DATABASE IF NOT EXISTS streamlit_app;
USE streamlit_app;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Optional: Create a user for the application
-- CREATE USER 'streamlit_user'@'*' IDENTIFIED BY 'your_password';
-- GRANT ALL PRIVILEGES ON streamlit_app.* TO 'streamlit_user'@'*';
-- FLUSH PRIVILEGES;
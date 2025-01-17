-- Create DB.
CREATE DATABASE IF NOT EXISTS todo_app;

-- Use DB.
USE todo_app;

-- Create Table.
CREATE TABLE IF NOT EXISTS todo(
    id CHAR(36) PRIMARY KEY,
    todo VARCHAR(255) NOT NULL,
    details TEXT
);


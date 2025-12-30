CREATE DATABASE finance
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE finance_app;

CREATE TABLE transactions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date DATE NOT NULL, -- Date of the transaction
  amount DECIMAL(10,2) NOT NULL -- Stores transaction amount
	CHECK (amount > 0), -- Checks that amount is positive
  type ENUM('income', 'expense') NOT NULL,
  person ENUM() NOT NULL, -- Add names of persons who will use this database (e.g., 'Alice', 'Bob', 'Charlie')
  category ENUM() NOT NULL, -- Add categories relevant to your transactions (e.g., 'food', 'rent', 'salary')
  note VARCHAR(255), -- Optional note about the transaction
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

UPDATE mysql.user SET Grant_priv='Y', Super_priv='Y' WHERE User='root';
FLUSH PRIVILEGES;
CREATE DATABASE IF NOT EXISTS products_db;
USE products_db;
CREATE TABLE IF NOT EXISTS products (
	name VARCHAR(100) NOT NULL UNIQUE PRIMARY KEY,
	amountInStock INT UNSIGNED NOT NULL
)
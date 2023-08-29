-- SQL-команды для создания таблиц
CREATE TABLE employees (
	employee_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	title VARCHAR(100),
	birth_date DATE,
	notes VARCHAR(1000)
);

CREATE TABLE customers (
	customer_id VARCHAR(5) PRIMARY KEY,
	company_name VARCHAR(50),
	contact_name VARCHAR(50)
);

CREATE TABLE orders (
	order_id INT PRIMARY KEY,
	customer_id VARCHAR(5) NOT NULL,
	employee_id INT NOT NULL,
	order_date DATE,
	ship_city VARCHAR(50),
	CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
	CONSTRAINT fk_employee_id FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
);
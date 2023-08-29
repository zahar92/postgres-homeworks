"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


def csv_reader(path):
    """
    Получение данных из файла
    Parameters:
        path(str): путь к файлу
    Returns:
        list: Список строк файла
    """
    data = []
    with open(path) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            data.append(row)
    return data


conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='123'
)

try:
    with conn:
        with conn.cursor() as cur:
            customers = csv_reader('./north_data/customers_data.csv')
            # cur.execute("DELETE FROM customers")
            for customer in customers:
                cur.execute("INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)", (customer[0], customer[1], customer[2]))

            employees = csv_reader('./north_data/employees_data.csv')
            # cur.execute("DELETE FROM employees")
            for employee in employees:
                cur.execute("INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) "
                            "VALUES (%s, %s, %s, %s, %s, %s)", (employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))

            orders = csv_reader('./north_data/orders_data.csv')
            # cur.execute("DELETE FROM orders")
            for order in orders:
                cur.execute("INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) "
                            "VALUES (%s, %s, %s, %s, %s)",
                            (order[0], order[1], order[2], order[3], order[4]))
finally:
    conn.close()

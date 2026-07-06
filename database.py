import pymysql
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME


def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )


def get_all_employees():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return employees


def add_employee(name, salary):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO employees(name, salary) VALUES(%s,%s)",
        (name, salary)
    )

    connection.commit()

    cursor.close()
    connection.close()

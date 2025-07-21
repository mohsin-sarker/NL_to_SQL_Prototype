import sqlite3
from faker import Faker
import random

"""
Create users.db database to store registered users.
    - Create users table.
Create sample.db database for NL2SQL queries.
    - Create departments table.
    - Create employees table.
    - Create sales table.
"""
# -------------- Initialise Faker Object -----------
faker = Faker()


# --------------- Create Users Database -------------------
def create_user_db():
    # Create Connection to users.db database in the same directory
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Create new table into users database and drop if table exists
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """)

    conn.commit()
    conn.close()
    print("✅ Users database initialised and seeded successfully.")



# ------------------- Create Company Database ------------------
def create_company_db():
    # Create Connection to company.db database in the same directory
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    # Drop if company schema_tables exists
    cursor.execute("DROP TABLE IF EXISTS employees")
    cursor.execute("DROP TABLE IF EXISTS departments")
    cursor.execute("DROP TABLE IF EXISTS sales")
    
    # Create tables.
    cursor.executescript("""
        CREATE TABLE departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        
        
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            department_id INTEGER,
            address TEXT,
            FOREIGN KEY(department_id) REFERENCES departments(id)
        );


        CREATE TABLE sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER,
            amount REAL,
            sale_date TEXT,
            FOREIGN KEY(employee_id) REFERENCES employees(id)
        );
    """)
    
    # --------------- Insert Fake Data into (Employees, Departments, Sales) ----------------
    # Insert Fake Departments
    departments = ["Engineering", "Marketing", "Sales", "HR", "Finance"]
    for department in departments:
        cursor.execute("INSERT INTO departments (name) VALUES (?)", (department,))
    
    # Now get department IDs
    cursor.execute("SELECT id FROM departments")
    dep_ids = [row[0] for row in cursor.fetchall()]
    
    # Initialise some users and sales
    users = 20
    sales = 100
    
    # Insert Fake employees
    for _ in range(users):
        fname = faker.first_name()
        lname = faker.last_name()
        address = faker.address()
        dep_id = random.choice(dep_ids)
        cursor.execute(
            "INSERT INTO employees (first_name, last_name, department_id, address) VALUES (?, ?, ?, ?)",
            (fname, lname, dep_id, address)
        )
    
    # Now get employee IDs
    cursor.execute("SELECT id FROM employees")
    employee_ids = [row[0] for row in cursor.fetchall()]
    
    # Now Insert Fake sales
    for _ in range(sales):
        employee_id = random.choice(employee_ids)
        amount = round(random.uniform(100, 1000), 2)
        sale_date = faker.date_this_year()
        cursor.execute(
            "INSERT INTO sales (employee_id, amount, sale_date) VALUES (?, ?, ?)",
            (employee_id, amount, sale_date)
        )

    conn.commit()
    conn.close()
    print("✅ Company database initialized and seeded successfully.")
    
    

# ------------- Seed Everything -----------------
def seed():
    create_user_db()
    create_company_db()
    print("✅ Database created and seeded successfully.")



if __name__ == '__main__':
    seed()
    print("✅ Databases have been created and seeded successfully.")

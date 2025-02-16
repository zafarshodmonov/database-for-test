import sqlite3
from faker import Faker

# Initialize Faker
fake = Faker()

# Connect to SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect("customers.db")
cursor = conn.cursor()

# Create a customer table if it doesn’t exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    address TEXT
)
""")

# Insert fake customer data
for _ in range(10):  # Change the number to insert more records
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    address = fake.address()

    cursor.execute("INSERT INTO customer (name, email, phone, address) VALUES (?, ?, ?, ?)", 
                   (name, email, phone, address))

# Commit changes and close connection
conn.commit()
conn.close()

print("Fake customer data inserted successfully!")

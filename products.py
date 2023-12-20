import os
import mysql.connector
import csv
from decimal import Decimal
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()

select_query = "SELECT * FROM products"
cursor.execute(select_query)
original_products = cursor.fetchall()

# Make a copy of the original data
products = list(original_products)

# Write original data to CSV
with open('original_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Product ID", "Name", "Quantity in Stock", "Unit Price"])
    csv_writer.writerows(original_products)

update_query = "UPDATE products SET unit_price = unit_price * 1.1 WHERE product_id = %s"

for product in products:
    cursor.execute(update_query, (product[0],))

connection.commit()

cursor.execute(select_query)
updated_products = cursor.fetchall()

# Write updated data to CSV
with open('updated_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Product ID", "Name", "Quantity in Stock", "Unit Price"])
    csv_writer.writerows(updated_products)

cursor.close()
connection.close()

import os
import mysql.connector
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
products = cursor.fetchall()

print("Data from the 'products' table:")
for product in products:
    print(product)


update_query = "UPDATE products SET unit_price = unit_price * 1.1 WHERE product_id = %s"

for product in products:
    cursor.execute(update_query, (product[0],))


connection.commit()


cursor.execute(select_query)
updated_products = cursor.fetchall()

print("\nUpdated data from the 'products' table:")
for updated_product in updated_products:
    print(updated_product)


cursor.close()
connection.close()

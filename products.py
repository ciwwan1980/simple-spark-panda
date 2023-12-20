
import os
from dotenv import load_dotenv
import mysql.connector

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

cursor.execute("SELECT * FROM products")
result = cursor.fetchall()

print("Data from the 'products' table:")
for row in result:
    print(row)


cursor.close()
connection.close()

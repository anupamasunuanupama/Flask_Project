import mysql.connector

DB=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="health_care",
)
CR=DB.cursor(dictionary=True)
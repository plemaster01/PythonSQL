# Create Table and DB in Python for SQL
import sqlite3

connection = sqlite3.connect('LeMasterTech.db')
cursor = connection.cursor()

# each entry will have - name, views, date (YYYY-MM-DD)
# sql command inside of triple quotes - MUST be written in SQL format
sql_command = """CREATE TABLE sample (
vid_name VARCHAR(30),
view_count INTEGER,
published DATE )"""
cursor.execute(sql_command)
connection.close()

# delete data from SQL using Python
import sqlite3
connection = sqlite3.connect('LeMasterTech.db')
cursor = connection.cursor()

cursor.execute('''DELETE FROM sample WHERE vid_name = "controls top 5";''')

connection.commit()
connection.close()

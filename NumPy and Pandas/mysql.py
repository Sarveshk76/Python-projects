import mysql.connector
conn_obj = mysql.connector.connect(host="localhost", user="root", passwd="admin123", database="mydatabase")
print(conn_obj)
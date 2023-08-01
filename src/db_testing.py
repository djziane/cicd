import mysql.connector

# cnx = mysql.connector.connect(user='root', password='pass',
#                               host='127.0.0.1',
#                               database='pytesting')
# cursor = cnx.cursor()
# cursor.execute("select aa from pytesting")
# record = cursor.fetchone()
# print("You're connected to database: ", record[0])
# cnx.close()


import pyodbc
print(pyodbc.drivers())
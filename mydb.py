import mysql.connector
#from mysql import connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'pradeep',
    passwd = 'Password@123', 
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crmdemo")

print("ALL Done")
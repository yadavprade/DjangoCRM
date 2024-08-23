import mysql.connector
#from mysql import connector

dataBase = mysql.connector.connect(
    host = 'py-djangocrm-githubactions-server.mysql.database.azure.com',
    user = 'enxygaclyh',
    passwd = '0ATma$nzeN9Xanex', 
)

cursorObject = dataBase.cursor()

cursorObject.execute("SHOW DATABASES")

print("ALL Done")

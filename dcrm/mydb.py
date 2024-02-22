import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Mh14@@6640',
    auth_plugin='mysql_native_password'
)

cursorObject = dataBase.cursor()

# Create database
cursorObject.execute("CREATE DATABASE elderco")

print("ALL Done!")
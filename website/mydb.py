import mysql.connector
database = mysql.connector.connect(
  host='localhost',
  user ='root',
  passwd='123456'

 )

cursorObject= database.cursor()
cursorObject.execute("create database elderco")
print("all done")
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="id1731846_marsplus"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM table1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

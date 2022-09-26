import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root", passwd="admin", database="world")

mycursor=mydb.cursor()

mycursor.execute("select * from city where CountryCode='IND' && District='Uttar Pradesh'")

for x in mycursor:
    print(x)
    
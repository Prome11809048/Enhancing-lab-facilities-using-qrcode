import mysql.connector

db1= mysql.connector.connect(host="localhost",user='root',password='Prome11809048',database ='qrcode')
print("Connection sucessful")

cur = db1.cursor()

#cur.execute('CREATE DATABASE Qrcode')
#cur.execute('CREATE TABLE details(Serail_no int PRIMARY KEY AUTO_INCREMENT,name varchar(30))')
#cur.execute("ALTER TABLE details RENAME COLUMN Serail_no TO Serial_no")
#cur.execute("ALTER TABLE details DROP COLUMN Serial_no")
#cur.execute("ALTER TABLE details ADD Type varchar(30)")
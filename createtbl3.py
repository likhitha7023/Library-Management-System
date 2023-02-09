#!C:\Program Files (x86)/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\sai rohit\\appdata\\roaming\\python\\python38\\site-packages')

import cgi

import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="",database="pro")
m = mydb.cursor()
m.execute("CREATE TABLE bklist(bookname varchar(50),author varchar(30),bid varchar(15),publications varchar(30),count varchar(3),date varchar(15))")
mydb.commit()
print("Table Created Successfully")
mydb.close()

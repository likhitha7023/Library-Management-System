#!C:\Program Files (x86)/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\sai rohit\\appdata\\roaming\\python\\python38\\site-packages')

import cgi

import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="",database="pro")
m = mydb.cursor()
m.execute("CREATE TABLE isubklist(id varchar(30),bookname varchar(50),bookid varchar(15),author varchar(30),issuedate varchar(15))")
mydb.commit()
print("Table Created Successfully")
mydb.close()

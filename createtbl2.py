#!C:\Program Files (x86)/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\sai rohit\\appdata\\roaming\\python\\python38\\site-packages')

import cgi

import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="",database="pro")
m = mydb.cursor()
m.execute("CREATE TABLE reg(name VARCHAR(30),id VARCHAR(30),password VARCHAR(15),phonenumber VARCHAR(10),gender VARCHAR(15),log VARCHAR(10),course VARCHAR(10),branch VARCHAR(10))")
mydb.commit()
print("Table Created Successfully")
mydb.close()

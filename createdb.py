#!C:\Program Files (x86)/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\sai rohit\\appdata\\roaming\\python\\python38\\site-packages')

import cgi

import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="")
m=mydb.cursor()
m.execute("CREATE DATABASE pro")
print("Database Created Successfully")

#!C:\Program Files (x86)/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\sai rohit\\appdata\\roaming\\python\\python38\\site-packages')

import cgi

import cgitb
import pymysql
cgitb.enable()
form=cgi.FieldStorage()

bkn=form.getvalue('bn')
auth=form.getvalue('au')
bd=form.getvalue('bid')
pbs=form.getvalue('pb')
c=form.getvalue('noc')
dt=form.getvalue('dt')

con=pymysql.connect(user='root',password='',host='localhost',database='pro')
cur=con.cursor()
sql="INSERT INTO bklist(bookname,author,bid,publications,count,date)values(%s,%s,%s,%s,%s,%s)"
val=(bkn,auth,bd,pbs,c,dt)
cur.execute(sql,val)
con.commit()
con.close()
print('''<html>
<body align="center">
<h1><b>Book added successfully</b></h1>
</body>
<html>''')

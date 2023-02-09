#!C:\Program Files (x86)/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\sai rohit\\appdata\\roaming\\python\\python38\\site-packages')

import cgi

import cgitb
import pymysql
cgitb.enable()


form=cgi.FieldStorage()

ide=form.getvalue('unm')
bid=form.getvalue('bid')

con=pymysql.connect(host="localhost",user="root",password="",database="pro")
cur=con.cursor()

cur.execute("select * from isubklist")
result=cur.fetchall()
res=0
for rows in result:
    if(rows[0]==ide):
        res=1
    
if(res):
    cur.execute("delete from isubklist where id=%s",(ide))
    con.commit()
    con.close()
    print('''<html>
<body align="center">
<h1><b>Book returned successfully by</b></h1>
</body>
<html>''')
    print(ide)
else:
    print('''<html>
<body align="center">
<h1><b>Book already returned!</b></h1>
</body>
<html>''')
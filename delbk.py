#!C:\Program Files (x86)/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\sai rohit\\appdata\\roaming\\python\\python38\\site-packages')

import cgi
import cgitb
import pymysql
cgitb.enable()

form=cgi.FieldStorage()
bd=form.getvalue('bid')

con=pymysql.connect(host="localhost",user="root",password="",database="pro")
cur=con.cursor()

cur.execute("select * from isubklist")
result=cur.fetchall()
res=1
for rows in result:
    if(rows[2]==bd):
        res=0

if(res):
    cur.execute("delete from bklist where bid=%s",(bd))
    con.commit()
    con.close()
    print('''<html>
<body align="center">
<h1><b>Book deleted successfully</b></h1>
</body>
<html>''')
else:
    print('''<html>
<body align="center">
<h1><b>Book can't be deleted it is already issued</b></h1>
</body>
<html>''')

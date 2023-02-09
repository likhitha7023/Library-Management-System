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

cur.execute("select * from reg")
result=cur.fetchall()
res=0
for rows in result:
    if(rows[1]==bd):
        res=1

if(res):
    cur.execute("delete from reg where id=%s",(bd))
    con.commit()
    con.close()
    print('''<html>
<body align="center">
<h1><b>User deleted successfully</b></h1>
</body>
<html>''')
else:
    print('''<html>
<body align="center">
<h1><b>User doesn't exist</b></h1>
</body>
<html>''')

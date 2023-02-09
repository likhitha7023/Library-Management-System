#!C:\Program Files (x86)/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\sai rohit\\appdata\\roaming\\python\\python38\\site-packages')

import cgi

import cgitb
import pymysql
cgitb.enable()
form=cgi.FieldStorage()


ide=form.getvalue('uid')
bknm=form.getvalue('bn')
bid=form.getvalue('bid')
auth=form.getvalue('au')
isdt=form.getvalue('isd')

con=pymysql.connect(host="localhost",user="root",password="",database="pro")
mycursor=con.cursor()

mycursor.execute("select * from reg")
res=0
result=mycursor.fetchall()
for rows in result:
    if(rows[1]==ide):
        res=1
        
if(res):
    sql="insert into isubklist(id,bookname,bookid,author,issuedate)values(%s,%s,%s,%s,%s)"
    val=(ide,bknm,bid,auth,isdt)
    mycursor.execute(sql,val)
    con.commit()
    con.close()
    print('''<html>
<body align="center">
<h1><b>Book issued successfully to</b></h1>
</body>
<html>''')
    print(ide)
else:
    print('''<html>
<body align="center">
<h1><b>This User id is not registered</b></h1>
</body>
<html>''')

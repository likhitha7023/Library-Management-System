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
pwd=form.getvalue('pswd')
mydb=pymysql.connect(host="localhost",user="root",password="",database="pro")
mycursor=mydb.cursor()
mycursor.execute("select id from isubklist where id")
res=mycursor.fetchall()

res=0
mycursor.execute("select * from reg")
r2=mycursor.fetchall()
for rows in r2:
    if(rows[1]==ide):
        res=1
mycursor.execute("select * from reg")
r3=mycursor.fetchall()
for rows in r3:
    if(rows[2]==pwd):
        res=2

if(res==2):
    mycursor.execute("select * from isubklist where id=%s",(ide))
    res=mycursor.fetchall()
    print("<table border='10'>")
    print("<tr><td>id</td><td>book name</td><td>bid</td><td>author</td><td>issue date</td></tr>")
    for rows in res:
        print("<tr>")
        for r in rows:
            print("<td>")
            print(r)
            print("</td>")
        print("</tr>")
    print("</table>")
else:
    print("Invalid credentials")
          

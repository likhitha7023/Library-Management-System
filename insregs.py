#!C:\Program Files (x86)/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\sai rohit\\appdata\\roaming\\python\\python38\\site-packages')

import cgi
import cgitb
import pymysql
cgitb.enable()

form=cgi.FieldStorage()

nme=form.getvalue('nm')
ide=form.getvalue('uid')
psd=form.getvalue('up')
phno=form.getvalue('upn')
gndr=form.getvalue('ug')
srt=form.getvalue('rag')
crs=form.getvalue('crs')
bnch=form.getvalue('brnch')

con=pymysql.connect(user='root',password='',host='localhost',database='pro')
cur=con.cursor()
cur.execute("select * from reg")
res=1
full=cur.fetchall()
for rows in full:
    if(rows[1]==ide):
        res=0
        break

if(res):
    sql="INSERT INTO reg(name,id,password,phonenumber,gender,log,course,branch)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(nme,ide,psd,phno,gndr,srt,crs,bnch)
    cur.execute(sql,val)
    con.commit()
    con.close()
    print("Registered Successfully")
else:
    print("Userid already exist ")
    

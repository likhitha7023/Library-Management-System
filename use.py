#!C:\Program Files (x86)/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\sai rohit\\appdata\\roaming\\python\\python38\\site-packages')

import cgi

import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="",database="pro")
mycursor=mydb.cursor()
mycursor.execute("select * from reg")
result=mycursor.fetchall()
print("<table border='10' align='center'>")
print("<tr><td>name</td><td>id</td><td>password</td><td>phone number</td><td>gender</td><td>logged as</td><td>course</td><td>branch</td></tr>")
for rows in result:
    print("<tr>")
    for r in rows:
        print("<td>")
        print(r)
        print("</td>")
    print("</tr>")
print("</table>")
print('''<!doctype html>
<html>
<body align="center">
<br><br>
<button onclick="history.back()">back</button>
</form>
</body></html>''')
    
    
mydb.commit()
mydb.close()
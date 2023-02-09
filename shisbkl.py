#!C:\Program Files (x86)/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\sai rohit\\appdata\\roaming\\python\\python38\\site-packages')

import cgi

import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="",database="pro")
mycursor=mydb.cursor()
mycursor.execute("select * from isubklist")
res=mycursor.fetchall()
print("<table border='10' align='center'>")
print("<tr><td>id</td><td>book name</td><td>bid</td><td>author</td><td>issue date</td></tr>")
for rows in res:
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
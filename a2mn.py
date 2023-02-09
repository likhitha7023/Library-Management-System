#!C:\Program Files (x86)/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\sai rohit\\appdata\\roaming\\python\\python38\\site-packages')

import cgi

import cgitb
import pymysql
import webbrowser
cgitb.enable()

form=cgi.FieldStorage()
ide=form.getvalue('uid')
pwd=form.getvalue('pswd')
mydb=pymysql.connect(host="localhost",user="root",password="",database="pro")
mycursor=mydb.cursor()
if(ide=="admin" and pwd=="admin1pswd"):
    print('''<!DOCTYPE html>
<head>
  <style>
    @import url("https://fonts.googleapis.com/css2?family=Poppins&display=swap");
    body {
      font-family: "Poppins", sans-serif;
      background-image: url("https://i.pinimg.com/564x/8c/74/bb/8c74bb4e959d7211e27c10b5980cb970.jpg");
      background-repeat: no-repeat;
      background-size: cover; 
    }
    fieldset {
      background-color: #254133;
      backdrop-filter: blur(3px) saturate(180%);
      -webkit-backdrop-filter: blur(3px) saturate(180%);
      background-color: rgba(17, 25, 40, 0.5);
      border-radius: 12px;
      border: 1px solid rgba(255, 255, 255, 0.125);
      width:40vw;
    }
    .center {
      display: flex;
      justify-content: center;
    }
    legend {
      background-color: #cd5c5c;
      color: white;
      padding: 5px 10px;
      margin: 0 auto;
    }
    .out {
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 10px;
    }
    fieldset{
      padding:100px;
      margin:0 auto;
      display:table;
      width:1px;
      *display:inline;
      *width:auto;
      vertical-align:middle;
      text-align:left;
   }
    label {
      width: 50%;
      text-align: right;
      margin-right: 5px;
      color: white;
    }
    form input {
      border: none;
      padding: 5px;
      width: 100%;
      height: 30px;
      border-radius: 3px;
      font-size: 16px;
    }
#submit:hover{
background:#000;
color:#fff
}
  </style>
</head>
<body class="center">
  <fieldset>
    <legend>MENU</legend>
  <form action="hm.html">
    <button id="submit" type="submit"  name="add" align="center">HOME PAGE</button><br><br>
  </form>
  <form action="addbk.html">
    <button id="submit" type="submit"  name="add" align="center">ADD BOOK</button><br><br>
  </form>
  <form action="isubk.html">
    <button id="submit" type="submit"  name="issue" align="center">ISSUE BOOK</button><br><br>
  </form>
  <form action="delbk.html">
    <button id="submit" type="submit"  name="del" align="center">DELETE BOOK</button><br><br>
  </form>
  <form action="retbk.html">
    <button id="submit" type="submit"  name="ret" align="center">RETURN BOOK</button><br><br>
  </form>
  <form action="shbklist.py">
    <button id="submit" type="submit"  name="view" align="center">VIEW BOOK LIST</button><br><br>
  </form>
  <form action="shisbkl.py">
    <button id="submit" type="submit"  name="isued" align="center">ISSUED BOOK LIST</button><br><br>
  </form>
  <form action="use.py">
    <button id="submit" type="submit"  name="used" align="center">USERS IN</button><br><br>
  </form> 
  <form action="du.html">
    <button id="submit" type="submit"  name="duse" align="center">DELETE USER</button><br><br>
  </form>

</body>
</html>

''')
else:
    print('''<html>
<body align="center">
<h1><b>Invalid Credentials</b></h1>
</body>
<html>''')
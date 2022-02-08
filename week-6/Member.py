from flask import Flask, request, redirect, session, render_template
import mysql.connector
import os
from dotenv import load_dotenv

# 獲取密碼
load_dotenv()
dbpassword=os.getenv('db_connectpass')

# 連線資料庫
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password=dbpassword,
  database="website"
)
# 設定Flask
app=Flask(__name__)
app.secret_key="thissecretonlyiknow"

# 首頁
@app.route("/")
def home():
    if "Name" in session :
        return redirect("/member")
    else:
        return render_template("HomePage.html")

# 登入程序
@app.route("/signin", methods=["POST"])
def validate():
    accountName=request.form["accountName"]
    passWord=request.form["passWord"]
    mycursor = mydb.cursor()
    mycursor.execute('select username, password from `member`')
    myresult=mycursor.fetchall()
    if (accountName,passWord) in myresult:
        session["Name"]=accountName
        return redirect("/member")
    elif (accountName,passWord) not in myresult:
        return redirect("/error?message=帳號、或密碼輸入錯誤")
    elif accountName == "" or passWord == "":
        return redirect("/error?message=請輸入帳號、密碼")

# 註冊程序
@app.route("/signup", methods=["POST"])
def signup():
    nickName=request.form["Name"]
    accountName=request.form["accountName"]
    passWord=request.form["passWord"]
    mycursor = mydb.cursor()
    mycursor.execute('select username from `member`')
    myresult=mycursor.fetchall()
    if (accountName,) not in myresult and nickName!="" and passWord!="" and accountName!="":
        mycursor = mydb.cursor()
        sql="insert into `member` (name, username, password) values (%s, %s, %s)"
        val=(nickName,accountName,passWord)
        mycursor.execute(sql,val)
        mydb.commit()
        return redirect("/")
    elif (accountName,) in myresult:
        return redirect("/error?message=帳號已經被註冊")
    else:
        return redirect("/error?message=註冊資料不可留空")

# 會員頁
@app.route("/member")
def logIn_Success():
    if "Name" in session :
      accountName=session["Name"]
      return render_template("member.html", name=accountName)
    else:
      return redirect("/")

# 錯誤頁
@app.route("/error")
def logIn_Fail():
    msg=request.args.get("message","登入失敗")
    return render_template("error.html", message=msg)

# 登出程序
@app.route("/signout")
def signout():
    del session["Name"]
    return redirect("/")

# if __name__ == "__main__":
app.run(port=3000)
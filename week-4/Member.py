from flask import Flask
from flask import request
from flask import redirect
from flask import session
from flask import render_template

app=Flask(__name__)
app.secret_key="thissecretonlyiknow"


@app.route("/")
def home():
    if "Name" in session :
        return redirect("/member")
    else:
        return render_template("HomePage.html")

@app.route("/signin", methods=["POST"])
def validate():
    accountName=request.form["accountName"]
    passWord=request.form["passWord"]
    if accountName == "test" and passWord == "test" :
        session["Name"]=accountName
        return redirect("/member")
    elif accountName == "" or passWord == "":
        return redirect("/error?message=請輸入帳號、密碼")
    else :
        return redirect("/error?message=帳號、或密碼輸入錯誤")

@app.route("/member")
def logIn_Success():
    if "Name" in session :
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def logIn_Fail():
    msg=request.args.get("message","登入失敗")
    return render_template("error.html", message=msg)

@app.route("/signout")
def signout():
    del session["Name"]
    return redirect("/")

# if __name__ == "__main__":
app.run(port=3000)
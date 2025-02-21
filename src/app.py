from flask import Flask,render_template,request,redirect,url_for,flash
from config import Config
from forms.LoginForm import LoginForm
from forms.RegisterForm import RegisterForm

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html",form=LoginForm())
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        flash("Data sent properly")
        print(email,password)
        return redirect(url_for("login"))


@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html",form=RegisterForm())
    elif request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        flash("Data sent properly")
        print(name,username,password,email)
        return redirect(url_for("register"))


if __name__ == "__main__":
    app.config.from_object(Config)
    app.run(debug=True)

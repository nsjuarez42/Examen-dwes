from flask import Flask,render_template,request,redirect,url_for,flash
from config import Config
from forms.LoginForm import LoginForm
from forms.RegisterForm import RegisterForm
from forms.TodoForm import TodoForm
from flask_login import current_user,LoginManager,login_user,login_required,logout_user
from flaskext.mysql import MySQL
from db.User import User
from db.Todo import Todo
from auth.UserAuth import UserAuth

app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager(app)
mysqlconn = MySQL(app)

def create_user_auth(userdata):
    #creates userauth object from tuple retrieved from mysql
    id,name,username,password,email = userdata
    return UserAuth(id,name,username,password,email)

@login_manager.user_loader
def load_user(id):
    cursor = mysqlconn.get_db().cursor()
    user_db = User.get_by_id(id,cursor)
    print("User from db is {}".format(user_db))
    return create_user_auth(user_db)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("todos"))
    
    if request.method == "GET":
        return render_template("login.html",form=LoginForm())
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        print("Email: {}, Password:{}".format(email,password))
        cursor = mysqlconn.get_db().cursor()
        user = User.get_by_mail(email,cursor)
        print(user)
        if not user:
            flash("User not found")
            return redirect(url_for("login"))
        if not UserAuth.check_password(user[3],password):
            flash("Invalid credentials")
            return redirect(url_for("login"))
        

        login_user(create_user_auth(user))
        return redirect(url_for("todos"))
        


@app.route("/register",methods=["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("todos"))
    
    if request.method == "GET":
        return render_template("register.html",form=RegisterForm())
    elif request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        cursor = mysqlconn.get_db().cursor()

        hashed = UserAuth.hash_password(password)
        created = User.insert(mysqlconn.get_db(),cursor,name,username,hashed,email)
        print("Created user is {}".format(created))
        flash("Data sent properly")
        print(name,username,password,email)
        return redirect(url_for("register"))

@app.route("/todos",methods=["GET","POST"])
@login_required
def todos():
    if request.method == "GET":

        print(current_user.id)
        todos = Todo.get_by_user_id(current_user.id,mysqlconn.get_db().cursor())
        return render_template("todos.html",form=TodoForm(),todos=todos)

    elif request.method == "POST": 
        title = request.form.get("title")
        description = request.form.get("description")
        db = mysqlconn.get_db()
        cursor = db.cursor()

        Todo.insert(db,cursor,title,description,current_user.id)
        print("Received {} {}".format(title,description))
        flash("Todo added successfully")
        return redirect(url_for("todos"))
    
@app.route("/admin")
@login_required
def admin():
    if current_user.username != "admin":
        return redirect(url_for("todos"))
    users = User.get_all(mysqlconn.get_db().cursor())
    return render_template("admin.html",users=users)
    
@app.route("/signout",methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, session
from env import KEY
from user import User
app = Flask(__name__)
app.secret_key = KEY

@app.route("/")
def index():
    return redirect('/users')

@app.route('/users/new')
def new():
    return render_template("create.html")

@app.route("/create",methods=["POST"])
def create_user():
    print(request.form)
    data = request.form
    User.save(data)
    # Don't forget to redirect after saving to the database
    return redirect("/users")

@app.route('/users')
def display_users():
    users = User.get_all()
    return render_template("users.html",all_users = users)

if __name__ == "__main__":
    app.run(debug=True)
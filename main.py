from flask import Flask,render_template,redirect,url_for,Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from views import views
from auth import auth
from models import User, db,Post,Comment,Like
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = "helloworld"
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///Blogpost.db"
app.app_context().push()
db.init_app(app)


app.register_blueprint(auth, url_prefix="/")
app.register_blueprint(views, url_prefix="/")

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route("/")
def home():
    return "<h1>Home</h1>"

@app.route("/profile")
def profile():
    return "<h1>profile</h1>"

if __name__ == "__main__":
    app.run(debug=True)
db.create_all()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY']='j43lkj558vgnvo438uvn'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'abraham1493@gmail.com'
app.config['MAIL_PASSWORD'] = 'Mariam112087!!'
mail = Mail(app)
# from innoviuzsite.users.routes import users
from innoviuzsite.posts.routes import posts
from innoviuzsite.main.routes import main
# app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)

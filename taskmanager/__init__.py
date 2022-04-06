import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECREY_KEY")
app.config["SQLALCHEMY_DATABASE_URL"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from taskmanager import routes
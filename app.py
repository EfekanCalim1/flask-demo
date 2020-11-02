from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] =  "sqlite:///data.db"

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(root= '0.0.0.0', debug=True)

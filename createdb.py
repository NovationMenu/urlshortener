from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url.db'

db = SQLAlchemy(app)

class Link(db.Model):
    __tablename__ = 'link'
    
    id  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(100), unique=True, nullable=False)
    
    def __init__(self, url):
        self.url = url
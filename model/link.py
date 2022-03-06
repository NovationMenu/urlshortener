from model.db import db

class Link(db.Model):
    __tablename__ = 'link'
    
    id  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(100), unique=True, nullable=False)
    
    def __init__(self, url):
        self.url = url
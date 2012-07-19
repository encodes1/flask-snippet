from app import db
from app.snip import constants as SNIP


class Snippet(db.Model):
    __tablename__ = 'Snippet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    type = db.Column(db.String(50))
    code = db.Column(db.String(500))

    def __init__(self, name=None, type=None, code=None):
        self.name = name
        self.type = type
        self.code = code

    def getCode(self):
        return self.code

    def __repr__(self):
        return '<User %r>' % (self.name)

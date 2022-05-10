from models import db


class CatModel(db.Model):
    __tablename__ = 'cat'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<cat {}>'.format(self.name)


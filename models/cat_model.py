from models import db


class Cat(db.Model):
    __tablename__ = 'cat'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __init__(self, name, post_id):
        self.name = name
        self.post_id = post_id

    def __repr__(self):
        return '<cat {}>'.format(self.name)


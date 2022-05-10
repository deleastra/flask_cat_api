from models import db


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cats = db.relationship('cats', backref='post', lazy=True)
    comments = db.relationship('comments', backref='post', lazy=True)

    def __init__(self, text, user_id, cats):
        self.text = text
        self.user_id = user_id
        self.cats = cats

    def __repr__(self):
        return '<Post {}>'.format(self.text)


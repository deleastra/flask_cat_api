from models import db


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __init__(self, text, post_id):
        self.text = text
        self.post_id = post_id

    def __repr__(self):
        return '<Comment {}>'.format(self.text)


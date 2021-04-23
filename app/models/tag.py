from app import db


class Tag(db.Model):
    __tablename__ = 't_tag'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True, comment='标签名')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tag %r>' % self.name

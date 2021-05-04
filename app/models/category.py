from app import db


class Category(db.Model):
    __tablename__ = 't_category'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True, comment='分类名称')
    slug = db.Column(db.String(64), nullable=False, unique=True, comment='分类别名')
    parentid = db.Column(db.Integer, db.ForeignKey('t_category.id'), comment='父分类ID')
    post = db.relationship('Post', backref=db.backref('t_category'), lazy='dynamic')
    description = db.Column(db.String(256), comment='分类描述')

    def __init__(self, **kwargs):
        super(Category, self).__init__(**kwargs)

    def __repr__(self):
        return '<Category %r>' % self.name

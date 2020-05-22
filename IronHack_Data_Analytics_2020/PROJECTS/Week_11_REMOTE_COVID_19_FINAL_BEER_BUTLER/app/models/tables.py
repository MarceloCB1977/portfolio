from app import db


class Beer_Table(db.Model):
    __tablename__ = 'beer'

    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.String(255), nullable=False)
    style_name = db.Column(db.String(255), nullable=False)
    recommend = db.Column(db.String(255), nullable=False)
    age = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(10), nullable=False)


    def __init__(self, index, style_name, recommend, age, gender):
        self.index = index
        self.style_name = style_name
        self.recommend = recommend
        self.age = age
        self.gender = gender

    def __repr__(self):
        return '<Beer_Table %r>' % self.style_name

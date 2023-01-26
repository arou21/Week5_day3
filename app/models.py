from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

# create models from out ERD
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False, unique=True)
    last_name = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    # post = db.relationship("Post", backref='author', lazy=True)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()


        
#this can be removed
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     img_url = db.Column(db.String, nullable=False)
#     caption = db.Column(db.String(1000))
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __init__(self, first_name, last_name, email, password):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.password = password

    # end of remove
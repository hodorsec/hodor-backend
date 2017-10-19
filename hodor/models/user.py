# -*- coding: utf-8 -*-

from hodor import db

class User(db.Model):
    __tablename__ = 'users'

    # Values entered by the user
    username = db.Column(db.String(32), primary_key=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)

    # Platform values
    disabled = db.Column(db.Boolean, default=False)
    verified_account = db.Column(db.Boolean, default=False)
    verification_code = db.Column(db.String(32), nullable=False)

    def __unicode__(self):
        return unicode(self.username)

    def __init__(self, name):
        """initialize with name."""
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<User: {}>".format(self.name)
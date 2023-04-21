import datetime

import sqlalchemy as sa
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import orm

from . db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    news = orm.relationship("News", back_populates='user')
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    about = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, index=True, unique=True, nullable=True)
    hashed_password = sa.Column(sa.String, index=True, nullable=True)
    creation_date = sa.Column(sa.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        global name, email
        return f'{self.name}, {self.email}\n'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

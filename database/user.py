import sqlalchemy as db

from database.base import Base


class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(length=100), unique=True, nullable=False)
    password = db.Column(db.String(length=255), nullable=False)
    email = db.Column(db.String(length=255), unique=True, nullable=False)
    phone = db.Column(db.String(length=11))
    last_login = db.Column(db.DateTime(timezone=True), nullable=True, default=None)

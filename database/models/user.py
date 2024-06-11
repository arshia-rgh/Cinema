import sqlalchemy as db
from sqlalchemy.orm import relationship

from database.base import Base


class User(Base):
    """
    A User entity representing a user in the database.
    - Attributes:
        - id (int): The UNIQUE identifier of the comment.
        - username (str): username of the user.
        - password (str): hashed password of the user.
        - email (str): UNIQUE email adderess of the user.
        - phone (str): phone number of the user.
        - last_login (datetime): last login date of the user
    - Relationships:
        - manager: one-to-one relationship with Manager if user is a manager
        - customer: one-to-one relationship with Customer if user is a customer
        - comments: a list of Comments on movies did by the user
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(length=100), unique=True, nullable=False)
    password = db.Column(db.String(length=255), nullable=False)
    email = db.Column(db.String(length=255), unique=True, nullable=False)
    phone = db.Column(db.String(length=11))
    last_login = db.Column(db.DateTime(timezone=True), nullable=True, default=None)

    manager = relationship('Manager', back_populates='user', uselist=False)
    customer = relationship('Customer', back_populates='user', uselist=False)
    comments = relationship('Comment', back_populates='user',cascade="all, delete")

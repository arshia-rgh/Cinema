import sqlalchemy as db
from sqlalchemy.orm import relationship

from database.base import Base


class Customer(Base):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    wallet = db.Column(db.Float, nullable=False, default=0.0)
    birth_date = db.Column(db.Date)
    registration_date = db.Column(db.DateTime, default=db.func.now())

    user = relationship('User', back_populates='customer')

    movie_rates = relationship('MovieRate', back_populates='customer',cascade="all, delete")
    cinema_rates = relationship('CinemaRate', back_populates='customer',cascade="all, delete")
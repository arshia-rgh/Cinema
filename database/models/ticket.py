import sqlalchemy as db
from sqlalchemy.orm import relationship

from database.base import Base


class Ticket(Base):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seat_id = db.Column(db.Integer, db.ForeignKey('sans_seats.id'), nullable=False)
    sans_id = db.Column(db.Integer, db.ForeignKey('sans.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    purchased_date = db.Column(db.DateTime(timezone=True), nullable=False)

    seat = relationship('SansSeat', back_populates='ticket')
    sans = relationship('Sans', back_populates='tickets')
    movie = relationship('Movie', back_populates='tickets')


import sqlalchemy as db
from sqlalchemy.orm import relationship

from database.base import Base


class Ticket(Base):
    """
    The Ticket model represents a ticket in the database.

    Attributes:
        id (int): The unique identifier of the ticket.
        seat_id (int): The identifier of the seat associated with the ticket.
        sans_id (int): The identifier of the sans associated with the ticket.
        movie_id (int): The identifier of the movie associated with the ticket.
        price (float): The price of the ticket.
        purchased_date (datetime): The date and time when the ticket was purchased.
        seat (relationship): The relationship between the Ticket and SansSeat models.
        sans (relationship): The relationship between the Ticket and Sans models.
        movie (relationship): The relationship between the Ticket and Movie models.
    """
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
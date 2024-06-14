import sqlalchemy as db
from sqlalchemy.orm import relationship, backref

from database.base import Base

'''SansSeat has one to one relation with
    ticket class
'''
class SansSeat(Base):
    """
    A Sans entity representing a sans in the database.
    - Attributes:
        - id (int): The unique identifier of the sans-seat.
        - seat_number (int): The number of the particular seat.
        - is_reserved (bool): Shows whether the seat is reserved or not
        - sans_id (int): FK(sans.id) sans manager.
        - ticket_id (int): FK(ticket.id) ticket manager. nullable

    - Relationships:
        - sans: the Sanse which the seat belongs to
        - ticket: the Ticket which the seat belongs to
    """
        
    __tablename__ = 'sans_seats'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    sans_id = db.Column(db.Integer(), db.ForeignKey('sans.id'), nullable=False)
    seat_number = db.Column(db.Integer())
    is_reserved = db.Column(db.Boolean, default=False)
    ticket_id = db.Column(db.Integer(), db.ForeignKey('tickets.id'))

    sans = relationship('Sans')
    ticket = relationship('Ticket')

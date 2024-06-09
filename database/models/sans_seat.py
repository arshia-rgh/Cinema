import sqlalchemy as db
from sqlalchemy.orm import relationship, backref

from database.base import Base

'''SansSeat has one to one relation with
    ticket class
'''
class SansSeat(Base):
    __tablename__ = 'sanss_seat'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    sans_id = db.Column(db.Integer(), db.ForeignKey('sans.id'), nullable=False)
    seat_number = db.Column(db.Integer())
    is_reserved = db.Column(db.Boolean, default=False)
    ticket_id = db.Column(db.Integer(), db.ForeignKey('tickets.id'))
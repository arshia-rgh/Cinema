import sqlalchemy as db
from sqlalchemy.orm import relationship

from database.base import Base

# this code is based on this document.
# https://medium.com/@mandyranero/one-to-many-many-to-many-and-one-to-one-sqlalchemy-relationships-8415927fe8aa

# TODO: the following code should be added to movie class  -> sans = relationship('sans', backref='movie')
# TODO: the following code should be added to cinema class -> sans = relationship('sans', backref='cinema')
'''The Sans class has one-to-many relation with:
    - Movie class
    - Cinema class

    - Sans_seat class
'''
class Sans(Base):
    __tablename__ = 'sans'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    
    capacity = db.Column(db.Integer())
    start_date = db.Column(db.DateTime(timezone=True), nullable=True, default=None)
    end_date = db.Column(db.DateTime(timezone=True), nullable=True, default=None)
    
    movie_id = db.Column(db.Integer(), db.ForeignKey('movie.id'), nullable=False)
    cinema_id = db.Column(db.Integer(), db.ForeignKey('cinema.id'), nullable=False)
    sans_seat = relationship('sans_seats', backref='sans')
import sqlalchemy as db
from sqlalchemy.orm import relationship

from database.base import Base

# this code is based on this document.
# https://medium.com/@mandyranero/one-to-many-many-to-many-and-one-to-one-sqlalchemy-relationships-8415927fe8aa

class Sans(Base):
    """
    A Sans entity representing a sans in the database.
    - Attributes:
        - id (int): The unique identifier of the sans.
        - capacity (int): The capacity of the particular sans.
        - start_date (dateTime): The start date of the sans.
        - end_date (dateTime): The end date of the sans.
        - movie_id (int): FK(movie.id) movie manager.
        - cinema_id (int): FK(cinema.id) cinema manager.

    - Relationships:
        - movie: the Movie which the sans belongs to
        - cinema: the Cinema which the sans belongs to
        - sans-seats: one to one relationship with Sansseat class
    """


    __tablename__ = 'sans'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    capacity = db.Column(db.Integer())
    start_date = db.Column(db.DateTime(timezone=True), nullable=True, default=None)
    end_date = db.Column(db.DateTime(timezone=True), nullable=True, default=None)

    movie_id = db.Column(db.Integer(), db.ForeignKey('movies.id'), nullable=False)
    cinema_id = db.Column(db.Integer(), db.ForeignKey('cinemas.id'), nullable=False)
    sans_seat = relationship('sans_seats', backref='sans')
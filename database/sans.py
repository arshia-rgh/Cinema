import sqlalchemy as db

from database.base import Base


class Sans(Base):
    __tablename__ = 'sans'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id'), nullable=False)
    
    capacity = db.Column(db.Integer)
    start_date = db.Column(db.DateTime(timezone=True), nullable=True, default=None)
    end_date = db.Column(db.DateTime(timezone=True), nullable=True, default=None)
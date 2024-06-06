import sqlalchemy as db

from database.base import Base


class SansSeat(Base):
    __tablename__ = 'sans_seat'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sans_id = db.Column(db.Integer, db.ForeignKey('sans.id'), nullable=False)
    seat_number = db.Column(db.Integer)
    is_reserved = db.Column(db.Boolean, nullable=True, default=False)
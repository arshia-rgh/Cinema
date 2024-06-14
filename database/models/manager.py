import sqlalchemy as db
from sqlalchemy.orm import relationship

from database.base import Base


class Manager(Base):
    __tablename__ = 'managers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.ForeignKey('users.id'), unique=True)

    user = relationship('User', back_populates='manager')
    cinemas = relationship('Cinema', back_populates='manager')

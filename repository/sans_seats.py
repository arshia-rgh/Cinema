from sqlalchemy.orm import Session
from typing import Type

from database.base import session
from database.models.sans_seat import SansSeat
from repository.base import BaseRepository


class SansSeatRepository(BaseRepository):

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Type[SansSeat]]:
        sans_seats: list[Type[SansSeat]] = self.db.query(SansSeat).all()
        return sans_seats

    def get_by_id(self, id: int) -> Type[SansSeat]:
        sans_seat = self.db.query(SansSeat).filter(SansSeat.id == id).first()
        if sans_seat:
            return sans_seat
        return None

    def create(self, item: SansSeat) -> SansSeat:
        try:
            seat = item
            self.db.add(item)
            self.db.commit()
            self.db.refresh(item)
            return seat
        except Exception as e:
            self.db.rollback()
            pass

    # TODO: rename SansSeat class to Seat
    def update(self, item: Type[SansSeat]) -> Type[SansSeat]:
        seat_db = self.db.query(SansSeat).filter(SansSeat.id == item.id).first()
        if seat_db:
            try:
                seat = item
                self.db.commit()
                self.db.refresh(seat)
                return seat
            except Exception as s:
                self.db.rollback()
                pass

        else:
            pass

    def delete(self, id: int) -> bool:
        seat = self.db.query(SansSeat).filter(SansSeat.id == id).first()
        if seat:
            self.db.delete(seat)
            self.db.commit()
            return True
        return False


seat_repository = SansSeatRepository(session)
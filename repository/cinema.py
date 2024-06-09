from typing import Type

from sqlalchemy.orm import Session

from database.base import session
from database.models.cinema import Cinema
from repository.base import BaseRepository


class CinemaRepository(BaseRepository):
    """
        All queries needed on cinemas are here. methods:
        - get_all
        - get_by_id
        - get_by_name
        - get_by_manager_id
        - create
        - update
        - delete
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Type[Cinema]] | None:
        cinemas: list[Type[Cinema]] = self.db.query(Cinema).all()
        return cinemas

    def get_by_id(self, id: int) -> Type[Cinema] | None:
        cinema = self.db.query(Cinema).filter(Cinema.id == id).first()
        if cinema:
            return cinema
        return None

    def get_by_name(self, name: str) -> Type[Cinema] | None:
        cinema = self.db.query(Cinema).filter(Cinema.name == name).first()
        if cinema:
            return cinema
        return None

    def get_by_manager_id(self, manager_id: int) -> Type[Cinema] | None:
        cinema = self.db.query(Cinema).filter(Cinema.manager_id == manager_id).first()
        if cinema:
            return cinema
        return None

    def create(self, item: Cinema) -> Cinema:
        try:
            self.db.add(item)
            self.db.commit()
            self.db.refresh(item)
            return item
        except Exception as e:
            self.db.rollback()
            # TODO: raise appropriate exception, Duplicate Manager or name
            pass

    def update(self, item: Type[Cinema]) -> Type[Cinema]:
        cinema = self.db.query(Cinema).filter(Cinema.id == item.id).first()
        if cinema:
            try:
                cinema = item
                self.db.commit()
                self.db.refresh(cinema)
                return cinema
            except Exception as e:
                self.db.rollback()
                # TODO: raise appropriate exception, Duplicate Manager_id or name
                pass

        else:
            # TODO: raise appropriate exception, Not found cinema
            pass

    def delete(self, id: int) -> bool:
        cinema = self.db.query(Cinema).filter(Cinema.id == id).first()
        if cinema:
            self.db.delete(cinema)
            self.db.commit()
            return True
        return False


cinema_repository = CinemaRepository(session)

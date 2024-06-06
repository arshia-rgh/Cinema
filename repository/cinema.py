from datetime import datetime

from sqlalchemy.orm import Session

from database.base import session
from database.cinema import Cinema
from database.manager import Manager
from schema.cinema import CinemaInDB, CinemaOutput


class CinemaRepository:
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

    def get_all(self) -> list[CinemaOutput] | None:
        cinema_db = self.db.query(Cinema).all()
        cinemas = [CinemaOutput(**cinema.__dict__) for cinema in cinema_db]
        return cinemas

    def get_by_id(self, id: int) -> CinemaOutput | None:
        cinema_db = self.db.query(Cinema).filter((Cinema).id == id).first()
        if cinema_db:
            cinema = CinemaOutput(**cinema_db.__dict__)
            return cinema
        return None

    def get_by_name(self, name: str) -> CinemaOutput | None:
        cinema_db = self.db.query(Cinema).filter(Cinema.name == name).first()
        if cinema_db:
            cinema = CinemaOutput(**cinema_db.__dict__)
            return cinema
        return None

    def get_by_manager_id(self, manager_id: int) -> CinemaOutput | None:
        cinema_db = self.db.query(Cinema).filter(Cinema.manager_id == manager_id).first()
        if cinema_db:
            cinema = CinemaOutput(**cinema_db.__dict__)
            return cinema
        return None

    def create(self, item: CinemaInDB) -> CinemaOutput:
        cinema_db = Cinema(**item.__dict__)
        try:
            self.db.add(cinema_db)
            self.db.commit()
            self.db.refresh(cinema_db)
            cinema = CinemaOutput(**cinema_db.__dict__)
            return cinema
        except Exception as e:
            # TODO: raise appropriate exception, Duplicate Manager or name
            pass

    def update(self, item: CinemaOutput) -> CinemaOutput:
        cinema_db = self.db.query(Cinema).filter(Cinema.id == item.id).first()
        if cinema_db:
            try:
                cinema_db.update(**item.__dict__)
                self.db.commit()
                self.db.refresh(cinema_db)
                cinema = CinemaOutput(**cinema_db.__dict__)
                return cinema
            except Exception as e:
                # TODO: raise appropriate exception, Duplicate Email or name
                pass

        else:
            # TODO: raise appropriate exception, Not found user
            pass

    def delete(self, id: int) -> bool:
        cinema_db = self.db.query(Cinema).filter(Cinema.id == id).first()
        if cinema_db:
            cinema_db.delete()
            self.db.commit()
            return True
        return False


Cinema_repository = CinemaRepository(session)

from typing import Type

from sqlalchemy.orm import Session

from database.base import session
from database.models.cinema_rate import CinemaRate
from repository.base import BaseRepository


class CinemaRateRepository(BaseRepository):
    """
        All queries needed on cinema_rates table are here.
        -   methods:
            - get_all           ( returns all cinema_rates )
            - get_by_id         ( returns a single cinema_rate )
            - get_by_customer_id    ( returns a list of all customer's cinema_rates )
            - get_by_cinema_id   ( returns a list of all rates on a cinema )
            - create
            - update
            - delete
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Type[CinemaRate]] | None:
        cinemaRates : list[Type[CinemaRate]] = self.db.query(CinemaRate).all()
        return cinemaRates

    def get_by_id(self, id: int) -> Type[CinemaRate] | None:
        cinemaRate = self.db.query(CinemaRate).filter(CinemaRate.id == id).first()
        if cinemaRate:
            return cinemaRate
        return None

    def get_by_customer_id(self, id: int) -> list[Type[CinemaRate]] | None:
        cinemaRates = self.db.query(CinemaRate).filter(CinemaRate.customer_id==id).all()
        if cinemaRates:
            return cinemaRates
        return None
    
    def get_by_cinema_id(self, id: int) -> list[Type[CinemaRate]] | None:
        cinemaRates = self.db.query(CinemaRate).filter(CinemaRate.cinema_id==id).all()
        if cinemaRates:
            return cinemaRates
        return None
           
    def create(self, item: CinemaRate) -> CinemaRate:
        try:
            self.db.add(item)
            self.db.commit()
            self.db.refresh(item)
            return item
        except Exception as e :
            self.db.rollback()
            # TODO: handle exceptions for invalid parameters (cinema,customer id)
            pass

    def update(self, item: Type[CinemaRate]) -> Type[CinemaRate]:
        cinemaRate = self.db.query(cinemaRate).filter(cinemaRate.id == item.id).first()
        if cinemaRate:
            try:
                cinemaRate = item
                self.db.commit()
                self.db.refresh(cinemaRate)
                return cinemaRate
            except Exception as e:
                self.db.rollback()
                # TODO: handle exceptions for invalid parameters (cinema,customer id)
                pass

        else:
            # TODO: raise appropriate exception, Not found cinemaRate
            pass

    def delete(self, id: int) -> bool:
        cinemaRate = self.db.query(CinemaRate).filter(CinemaRate.id == id).first()
        if cinemaRate:
            self.db.delete(cinemaRate)
            self.db.commit()
            return True
        return False


cinema_rate_repository = CinemaRateRepository(session)

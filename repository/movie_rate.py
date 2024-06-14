from typing import Type

from sqlalchemy.orm import Session
from sqlalchemy import func

from database.base import session
from database.models.movie_rate import MovieRate
from repository.base import BaseRepository

from utils.exceptions import RateCreationError


class MovieRateRepository(BaseRepository):
    """
        All queries needed on movie_rates table are here.
        -   methods:
            - get_all           ( returns all movie_rates )
            - get_by_id         ( returns a single movie_rate )
            - get_by_customer_id    ( returns a list of all customer's movie_rates )
            - get_by_movie_id   ( returns a list of all rates on a movie )
            - check_if_has_rated (returns True if the customer has rated the movie)
            - create
            - update
            - delete
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Type[MovieRate]] | None:
        movieRates : list[Type[MovieRate]] = self.db.query(MovieRate).all()
        return movieRates

    def get_by_id(self, id: int) -> Type[MovieRate] | None:
        movieRate = self.db.query(MovieRate).filter(MovieRate.id == id).first()
        if movieRate:
            return movieRate
        return None

    def get_by_customer_id(self, id: int) -> list[Type[MovieRate]] | None:
        movieRates = self.db.query(MovieRate).filter(MovieRate.customer_id==id).all()
        if movieRates:
            return movieRates
        return None
    
    def get_by_movie_id(self, id: int) -> list[Type[MovieRate]] | None:
        movieRates = self.db.query(MovieRate).filter(MovieRate.movie_id==id).all()
        if movieRates:
            return movieRates
        return None
    
    def check_if_has_rated(self, customer_id: int, movie_id:int) -> type[MovieRate] | None :
        movie_rate = self.db.query(MovieRate).filter(MovieRate.customer_id == customer_id and MovieRate.movie_id== movie_id).first()
        if movie_rate:
            return movie_rate
        return None

    def get_avg_rate(self, movie_id: int) -> float :
        avg = self.db.query(func.avg(MovieRate.stars)).filter(MovieRate.movie_id == movie_id)
        return avg

    def create(self, item: MovieRate) -> MovieRate:
        try:
            self.db.add(item)
            self.db.commit()
            self.db.refresh(item)
            return item
        except Exception as e :
            self.db.rollback()
            raise RateCreationError
            

    def update(self, item: Type[MovieRate]) -> Type[MovieRate]:
        movieRate = self.db.query(MovieRate).filter(MovieRate.id == item.id).first()
        if movieRate:
            try:
                movieRate = item
                self.db.commit()
                self.db.refresh(movieRate)
                return movieRate
            except Exception as e:
                self.db.rollback()
                # TODO: handle exceptions for invalid parameters (movie,customer id)
                pass

        else:
            # TODO: raise appropriate exception, Not found MovieRate
            pass

    def delete(self, id: int) -> bool:
        movieRate = self.db.query(MovieRate).filter(MovieRate.id == id).first()
        if movieRate:
            self.db.delete(movieRate)
            self.db.commit()
            return True
        return False


movie_rate_repository = MovieRateRepository(session)

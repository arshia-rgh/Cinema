from typing import Type

from sqlalchemy.orm import Session

from database.base import session
from database.models.movie_rate import MovieRate
from repository.base import BaseRepository


class MovieRateRepository(BaseRepository):
    """
        All queries needed on movie_rates table are here.
        -   methods:
            - get_all           ( returns all movie_rates )
            - get_by_id         ( returns a single movie_rate )
            - get_by_user_id    ( returns a list of all user's movie_rates )
            - get_by_movie_id   ( returns a list of all rates on a movie )
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

    def get_by_user_id(self, id: int) -> list[Type[MovieRate]] | None:
        movieRates = self.db.query(MovieRate).filter(MovieRate.user_id==id).all()
        if movieRates:
            return movieRates
        return None
    
    def get_by_movie_id(self, id: int) -> list[Type[MovieRate]] | None:
        movieRates = self.db.query(MovieRate).filter(MovieRate.movie_id==id).all()
        if movieRates:
            return movieRates
        return None
           
    def create(self, item: MovieRate) -> MovieRate:
        try:
            self.db.add(item)
            self.db.commit()
            self.db.refresh(item)
            return item
        except Exception as e :
            self.db.rollback()
            # TODO: handle exceptions for invalid parameters (movie,user id)
            pass

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
                # TODO: handle exceptions for invalid parameters (movie,user id)
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

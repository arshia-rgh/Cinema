from typing import Type

from sqlalchemy.orm import Session

from database.base import session
from database.models.movie import Movie
from repository.base import BaseRepository


class MovieRepository(BaseRepository):
    """
        All queries needed on movies are here. methods:
        - get_all
        - get_by_id
        - get_by_name
        - create
        - update
        - delete
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Type[Movie]] | None:
        movies : list[Type[Movie]] = self.db.query(Movie).all()
        return movies

    def get_by_id(self, id: int) -> Type[Movie] | None:
        movie = self.db.query(Movie).filter(Movie.id == id).first()
        if movie:
            return movie
        return None

    def get_by_name(self, name: str) -> Type[Movie] | None:
        movie = self.db.query(Movie).filter(Movie.name == name).first()
        if movie:
            return movie
        return None

    def create(self, item: Movie) -> Movie:
        try:
            self.db.add(item)
            self.db.commit()
            self.db.refresh(item)
            return item
        except Exception as e :
            # TODO: handle exceptions for rate and name values
            pass

    def update(self, item: Type[Movie]) -> Type[Movie]:
        movie = self.db.query(movie).filter(movie.id == item.id).first()
        if movie:
            try:
                movie = item
                self.db.commit()
                self.db.refresh(movie)
                return movie
            except Exception as e:
                # TODO: handle exceptions for rate and name values
                pass

        else:
            # TODO: raise appropriate exception, Not found movie
            pass

    def delete(self, id: int) -> bool:
        movie = self.db.query(Movie).filter(Movie.id == id).first()
        if movie:
            self.db.delete(movie)
            self.db.commit()
            return True
        return False

movie_repository = MovieRepository(session)

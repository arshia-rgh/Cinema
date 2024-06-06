from datetime import datetime

from sqlalchemy.orm import Session

from database.base import session
from database.movie import Movie
from schema.movie import MovieInDB, MovieOutput


class MovieRepository:
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

    def get_all(self) -> list[MovieOutput] | None:
        movie_db = self.db.query(Movie).all()
        movies = [MovieOutput(**movie.__dict__) for movie in movie_db]
        return movies

    def get_by_id(self, id: int) -> MovieOutput | None:
        movie_db = self.db.query(Movie).filter(Movie.id == id).first()
        if movie_db:
            movie = MovieOutput(**movie_db.__dict__)
            return movie
        return None

    def get_by_name(self, name: str) -> MovieOutput | None:
        movie_db = self.db.query(Movie).filter(Movie.name == name).first()
        if movie_db:
            movie = MovieOutput(**movie_db.__dict__)
            return movie
        return None

    def create(self, item: MovieInDB) -> MovieOutput:
        movie_db = movie(**item.__dict__)
        try:
            self.db.add(movie_db)
            self.db.commit()
            self.db.refresh(movie_db)
            movie = MovieOutput(**movie_db.__dict__)
            return movie
        except Exception as e :
            # TODO: handle exceptions for rate and name values
            pass

    def update(self, item: MovieOutput) -> MovieOutput:
        movie_db = self.db.query(movie).filter(movie.id == item.id).first()
        if movie_db:
            try:
                movie_db.update(**item.__dict__)
                self.db.commit()
                self.db.refresh(movie_db)
                movie = MovieOutput(**movie_db.__dict__)
                return movie
            except Exception as e:
                # TODO: handle exceptions for rate and name values
                pass

        else:
            # TODO: raise appropriate exception, Not found movie
            pass

    def delete(self, id: int) -> bool:
        movie_db = self.db.query(Movie).filter(Movie.id == id).first()
        if movie_db:
            movie_db.delete()
            self.db.commit()
            return True
        return False

movie_repository = MovieRepository(session)

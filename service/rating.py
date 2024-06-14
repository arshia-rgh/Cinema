from database import Cinema, CinemaRate, Movie, MovieRate
from repository.cinema import CinemaRepository, cinema_repository
from repository.cinema_rate import CinemaRateRepository, cinema_rate_repository

from repository.movie import MovieRepository, movie_repository
from repository.movie_rate import MovieRateRepository, movie_rate_repository

from repository.customer import CustomerRepository, customer_repository


from utils.exceptions import InvalidRateValueError, MovieNotFoundError, CustomerNotFoundError, alreadyRatedError


class MovieRateService:
    """
    A service class to handle movie rating by the customers.

    - Attributes:
        -   movie_rate_repository (BankAccountRepository): A repository for accessing movie_rate data
    - methods:
        -   rate_movie
        -   update_movie_rate
    """
    def __init__(self, movie_rate_repository: MovieRateRepository, movie_repository: MovieRepository, customer_repository:CustomerRepository):
        self.movie_rate_repo = movie_rate_repository
        self.movie_repo = movie_repository
        self.customer_repo = customer_repository


    def rate_movie(self, movie_id: int, customer_id: int, stars: int) -> bool:
        """
        Enables a customer to rate a movie. 
        Validates enteries and creates a row in movie_rates table
        After success, will update 'movies' table col "rate" as well

        - Args:
            movie_id (int): The ID of the movie.
            customer_id (int): The ID of the customer.
            stars (int): The given stars to the movie.

        - Returns:
                  bool: True if rating is successful, False otherwise.
        """
        # validate enteries
        if 5 < stars < 0:
            raise InvalidRateValueError
        
        movie = self.movie_repo.get_by_id(movie_id)
        if not movie:
            raise MovieNotFoundError
        
        customer = self.customer_repo.get_by_id(customer_id)
        if not customer:
            raise CustomerNotFoundError

        has_rated = self.movie_rate_repo.check_if_has_rated(customer_id, movie_id)
        if has_rated:
            raise alreadyRatedError
        #   create a MovieRate obj
        movie_rate = MovieRate(
            movie_id = movie_id,
            customer_id = customer_id,
            stars = stars
        )
        mr = self.movie_rate_repo.create(movie_rate)
        
        if mr:
            return True
        return False
    
    def update_movie_rate(self, movie_id) -> bool:
        """
        Calculates avg rate and updates the movie's rate in movies table.
        - Args:
            - movie_id
        - Returns:
            - bool : True if successful
        """
        #   calculae avg rate for the movie and update it.
        new_rate = self.movie_rate_repo.get_avg_rate(movie_id)
        update_state = self.movie_repo.update_rate(movie_id,new_rate)
        
        return update_state


movie_rate_service = MovieRateService(movie_rate_repository, movie_repository, customer_repository)

class CinemaRateService:
    pass
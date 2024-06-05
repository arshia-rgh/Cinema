from Movie import Movie
from Cinema import Cinema
import datetime


class Sans:
    def __init__(self, cinema: Cinema, movie: Movie, capacity: int, start_datetime: datetime.datetime,
                 end_datetime: datetime.datetime):
        self.cinema = cinema
        self.movie = movie
        self.capacity = capacity
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

    def __str__(self):
        return f"{self.cinema.name} - {self.movie.name} - {self.capacity} - {self.start_datetime} - {self.end_datetime}"

    @staticmethod
    def create_sans():
        # manager should enter the following info
        # movie = selected movie obj
        # cinema = selected cinema obj
        capacity = int(input("Enter capacity: "))
        start_datetime = input("Enter start date and time (yyyy-mm-dd hh:mm): ")
        end_datetime = input("Enter end date and time (yyyy-mm-dd hh:mm): ")
        # sans = Sans(cinema, movie, capacity, start_datetime, end_datetime)
        # add to database

    def get_all_sans(self):
        pass

    # need to implement db query to delete sans that are passed

    def delete_sans(self):
        # manager can delete a sans
        pass

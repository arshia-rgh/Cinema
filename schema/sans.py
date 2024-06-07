from dataclasses import dataclass
from datetime import datetime



@dataclass
class Sans:
    id: int
    movie_id: int
    cinema_id: int
    capacity: int
    start_date: datetime
    end_date: datetime

    def __init__(self, id:int, movie_id: int, cinema_id: int, capacity: int, \
                 start_date: datetime, end_date: datetime, *args, **kwargs):
        self.id = id
        self.movie_id = movie_id
        self.cinema_id = cinema_id
        self.capacity = capacity
        self.start_date = start_date
        self.end_date = end_date

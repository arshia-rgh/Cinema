from dataclasses import dataclass
from datetime import datetime



@dataclass
class Sans:
    movie_id: int
    cinema_id: int
    capacity: int
    start_date: datetime
    end_date: datetime

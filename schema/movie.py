from dataclasses import dataclass


@dataclass
class MovieInDB:
    name : str
    age_limit : int
    rate : int


@dataclass
class MovieOutput:
    id: int
    name : str
    age_limit : int
    rate : int
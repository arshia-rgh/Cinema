from dataclasses import dataclass


@dataclass
class CinemaInDB:
    name : str
    manager_id : int
    rate : int


@dataclass
class CinemaOutput:
    id: int
    name : str
    manager_id : int
    rate : int
from dataclasses import dataclass


@dataclass
class SansSeat:
    id: int
    sans_id: int
    seat_number: int
    is_reserved: bool

    def __init__(self, id: int, sans_id: int, seat_number: int, is_reserved: bool, *args, **kwargs):
        self.id = id
        self.sans_id = sans_id
        self.seat_number = seat_number
        self.is_reserved = is_reserved


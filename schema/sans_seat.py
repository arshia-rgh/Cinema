from dataclasses import dataclass


@dataclass
class SansSeat:
    id: int
    sans_id: int
    seat_number: int
    is_reserved: bool

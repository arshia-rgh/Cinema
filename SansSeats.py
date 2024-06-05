from Sans import Sans


class SansSeats:
    def __init__(self, sans: Sans, seat_number: int, is_reserved: bool = False):
        self.sans = sans
        self.seat_number = seat_number
        self.is_reserved = is_reserved

    def get_all_available_seats(self):
        # show all available seats for a sans (is_reserved = False)
        pass

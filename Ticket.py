from Sans import Sans
from SansSeats import SansSeats
from Movie import Movie
import datetime


class Ticket:
    def __init__(self, sans_seat: SansSeats, movie: Movie, price: int,
                 purchase_datetime: datetime.datetime = datetime.datetime.now()):
        self.sans_seat = sans_seat
        self.movie = movie
        self.price = price
        self.purchase_datetime = purchase_datetime

    def __str__(self):
        return f"{self.sans_seat.sans.cinema.name} - {self.sans_seat.sans.movie.name} - {self.sans_seat.seat_number} - {self.price}"

    def reserve_ticket(self):
        # reserve a ticket
        pass

    def get_all_reserved_tickets(self):
        pass

    def get_all_available_tickets(self):
        pass

    def cancel_ticket(self):
        # cancel a ticket
        pass

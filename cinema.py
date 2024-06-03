# import User and Manager classes

class Cinema:
    def __init__(self, name, manager: Manager, rate):
        self.name = name
        self.rate = rate
        self.manager = manager

    def add_rate(self):
        # add new rates to cinema rates table
        pass


class CinemaRate:
    def __init__(self, cinema: Cinema, score, user: User):
        self.cinema = cinema
        self.score = score
        self.user = user

    def get_rate(self):
        # after receiving new rate it return updated avg rate
        pass

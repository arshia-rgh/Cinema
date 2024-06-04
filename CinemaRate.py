from cinema import Cinema


class CinemaRate:
    def __init__(self, cinema: Cinema, score: int, user: User):
        self.cinema = cinema
        self.score = score
        self.user = user

    @staticmethod
    def create_rate(cinema: Cinema, score: int, user: User):
        # cinema = selected cinema object
        # user = selected user object
        score = int(input('Enter score:(0-5) ')
        if score < 0 or score > 5:
            raise ValueError('Score must be between 0 and 5')

        rate = CinemaRate(cinema, score, user)
        cinema.add_rate(rate)
        cinema.update_average_rate()
        # db query
        # insert new rate to rate table
        pass
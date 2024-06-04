# import Manager class
from CinemaRate import CinemaRate


class Cinema:
    def __init__(self, name: str, manager: Manager):
        self.name = name  # db column
        self.rates = []
        self.manager = manager  # db column
        self.average_rate = 0.0  # db column

    def add_rate(self, rate: CinemaRate):
        self.rates.append(rate)

    def update_average_rate(self):
        if self.rates:
            self.average_rate = sum(rate.score for rate in self.rates) / len(self.rates)
        else:
            return None

    @staticmethod
    def create_cinema(name, manager: Manager):
        name = input('Enter cinema name: ')
        # manager = selected manager object
        cinema = Cinema(name, manager)
        # db query
        # insert new cinema to cinema table
        pass

    def delete_cinema(self, name, manager: Manager):
        # db query
        # delete cinema from cinema table with given name
        pass

    def update_cinema(self, name, manager: Manager):
        # db query
        # update cinema from cinema table with given name
        pass

    def get_cinema_with_name(self, name, manager: Manager):
        # db query
        # get cinema from cinema table with given name
        pass

    def get_all_cinemas_order_by_rate(self):
        # db query
        # get all cinemas from cinema table and order by rate
        pass

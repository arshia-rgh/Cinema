from enum import Enum
from datetime import datetime


from utils.cli import clear_terminal
from repository.sans import Sans, sans_repository
from repository.movie import movie_repository
from repository.cinema import cinema_repository

# should be created by script
# generate sanses
# generate cinemas informations


class AdminMenuOption(Enum):
    SANS = 1
    CINEMA = 2
    MOVIE = 3
    EXIT = 4


class DetailMenuOption(Enum):
    CREATE = 1
    UPDATE = 2
    DELETE = 3
    SHOW_ALL = 4
    BACK = 5


def main_menu():
    print("Please select an option:")
    print("1. Sans")
    print("2. Cinema")
    print("3. Movie")
    print("4. Exit")
    option = int(input('Enter your option number: '))
    return option


def detail_menu():
    print("1. Create")
    print("2. Update")
    print("3. Remove")
    print("4. Show All")
    print("5. Back")
    option = int(input('Enter your option number: '))
    return option


def handle_sans_menu(selected):
    clear_terminal()
    if selected == DetailMenuOption.CREATE.value:
        # 1 -> show list of all movies
        movies = movie_repository.get_all()
        for movie in movies:
            print(movie.id, movie.name)

        movie_id = input("Movie ID: ")

        # 2 -> show list of all cinemas
        cinemas = cinema_repository.get_all()
        for cinema in cinemas:
            print(cinema.id, cinema.name)

        cinema_id = input("Cinema ID: ")

        start_date = input("Start Date: (example format: 1998-06-05): ")
        end_date = input("End Date: (example format: 1998-06-05): ")
        capacity = input("Capacity: ")

        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        sans = Sans(start_date=start_date, end_date=end_date, capacity=capacity, movie_id=movie_id, cinema_id=cinema_id)
        sans_repository.create(sans)

    elif selected == DetailMenuOption.SHOW_ALL.value:
        sanses = sans_repository.get_all()
        print("ID\tNAME\tSTART_DATE\tEND_DATE")
        for sans in sanses:
            print(f'{sans.id}:\t{sans.name}\t{sans.start_date}\t{sans.end_date}')

    elif selected == DetailMenuOption.DELETE.value:
        id = int(input("Enter the id of a sans: "))
        sans_repository.delete(id)
    
    elif selected == DetailMenuOption.UPDATE.value:
        # 1 -> show list of all movies
        movies = movie_repository.get_all()
        for movie in movies:
            print(movie.id, movie.name)

        movie_id = input("Movie ID: ")

        # 2 -> show list of all cinemas
        cinemas = cinema_repository.get_all()
        for cinema in cinemas:
            print(cinema.id, cinema.name)

        cinema_id = input("Cinema ID: ")

        start_date = input("Start Date: (example format: 1998-06-05): ")
        end_date = input("End Date: (example format: 1998-06-05): ")
        capacity = input("Capacity: ")

        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        sans = Sans(start_date=start_date, end_date=end_date, capacity=capacity, movie_id=movie_id, cinema_id=cinema_id)
        sans_repository.update(sans)

    elif selected == DetailMenuOption.BACK.value:
        return


def handle_cinema_menu(selected):
    pass


def handle_movie_menu(selected):
    pass


def admin_menu():
    while True:
        clear_terminal()
        print('Welcome to Adminestration of CinemaTicket CRM 🤩')
        selected = main_menu()

        if selected == AdminMenuOption.SANS.value:
            clear_terminal()
            print("Sans Adminestration Menu")
            sans_selected = detail_menu()
            handle_sans_menu(sans_selected)

            
        elif selected == AdminMenuOption.CINEMA.value:
            clear_terminal()
            print("Cinema Adminestration Menu")
            cinema_selected = detail_menu()
            handle_cinema_menu(cinema_selected)

        elif selected == AdminMenuOption.MOVIE.value:
            clear_terminal()
            print("Movie Adminestration Menu")
            movie_selected = detail_menu()
            handle_movie_menu(movie_selected)

        else:
            clear_terminal()
            print('Goodbye 👋')
            break


admin_menu()
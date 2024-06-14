from typing import Type

from sqlalchemy.orm import Session

from database.base import session
from database.models.ticket import Ticket
from repository.base import BaseRepository


class TicketRepository(BaseRepository):
    """
    A repository for managing Ticket entities in the database.

    This class provides methods for performing CRUD operations on Ticket entities in the database.
    It uses SQLAlchemy's Session object for querying the database.

    Attributes:
        db (Session): The database session to use for queries.
    """
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Type[Ticket]] | None:
        tickets = self.db.query(Ticket).all()
        return tickets

    def get_by_id(self, id: int) -> Type[Ticket] | None:
        ticket = self.db.query(Ticket).filter(Ticket.id == id).first()
        return ticket

    def get_by_seat_id(self, id: int) -> Type[Ticket] | None:
        ticket = self.db.query(Ticket).filter(Ticket.seat_id == id).first()
        return ticket

    def get_by_sans_id(self, id: int) -> list[Type[Ticket]] | None:
        tickets = self.db.query(Ticket).filter(Ticket.sans_id == id).all()
        return tickets

    def get_by_movie_id(self, id: int) -> list[Type[Ticket]] | None:
        tickets = self.db.query(Ticket).filter(Ticket.movie_id == id).all()
        return tickets

    def create(self, item: Ticket) -> Ticket:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def update(self, item: Type[Ticket]) -> type[Ticket] | None:
        ticket = self.db.query(Ticket).filter(Ticket.id == id).first()
        if ticket:
            ticket = item
            self.db.commit()
            self.db.refresh(ticket)
            return ticket
        return None

    def delete(self, id: int) -> bool:
        ticket = self.db.query(Ticket).filter(Ticket.id == id).first()
        if ticket:
            self.db.delete(ticket)
            self.db.commit()
            return True
        return False


ticket_repository = TicketRepository(session)

from sqlalchemy.orm import Session

from database.base import session
from database.sans_seat import SansSeat
from schema.sans_seat import SansSeat as scheam_sans_seats


class SansSeatRepository:

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[scheam_sans_seats]:
        query = self.db.query(SansSeat).all()
        sans_seats = [scheam_sans_seats(**sans_seat.__dict__) for sans_seat in query]
        return sans_seats
    
    def get_by_id(self, id: int) -> scheam_sans_seats:
        sans_seat_db = self.db.query(SansSeat).filter(SansSeat.id == id).first()
        if sans_seat_db:
            seat = scheam_sans_seats(**sans_seat_db.__dict__)
            return seat
        return None
    
    def create(self, item: scheam_sans_seats) -> scheam_sans_seats:
        seat_db = SansSeat(**item.__dict__)
        try:
            self.db.add(seat_db)
            self.db.commit()
            self.db.refresh(seat_db)
            seat = scheam_sans_seats(**seat_db.__dict__)
            return seat
        except Exception as e:
            pass


    def update(self, item: scheam_sans_seats) -> scheam_sans_seats:
        seat_db = self.db.query(SansSeat).filter(SansSeat.id == item.id).first()
        if seat_db:
            try:
                seat_db.update(**item.__dict__)
                self.db.commit()
                self.db.refresh(seat_db)
                seat = scheam_sans_seats(**seat_db.__dict__)
                return seat
            except Exception as s:
                pass
        
        else:
            pass


    def delete(self, id:int) -> bool:
        seat_db = self.db.query(SansSeat).filter(SansSeat.id == id).first()
        if seat_db:
            seat_db.delete()
            self.db.commit()
            return True
        return False
    
    
sans_seat_repository = SansSeatRepository(session)
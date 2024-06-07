from datetime import datetime

from sqlalchemy.orm import Session

from database.base import session
from database.sans import Sans
from schema.sans import Sans as SSans


class SansRepository:

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[SSans]:
        sans_db = self.db.query(Sans).all()
        sanses = [SSans(**sans.__dict__) for sans in sans_db]
        return sanses
    
    def get_by_id(self, id:int) -> SSans:
        sans_db = self.db.query(Sans).filter(Sans.id == id).first()
        if sans_db:
            sans = SSans(**sans_db.__dict__)
            return sans
        return None
    
    def create(self, item:SSans) -> SSans:
        sans_db = Sans(**item.__dict__)
        try:
            self.db.add(sans_db)
            self.db.commit()
            self.db.refresh(sans_db)
            sans = SSans(**sans_db.__dict__)
            return sans
        except Exception as e:
            pass

    def update(self, item:SSans) -> SSans:
        sans_db = self.db.query(Sans).filter(Sans.id == item.id).first()
        if sans_db:
            try:
                sans_db.update(**item.__dict__)
                self.db.commit()
                self.db.refresh(sans_db)
                sans = SSans(**sans_db.__dict__)
                return sans
            except Exception as e:
                pass
        else:
            pass

    def delete(self, id: int) -> bool:
        sans_db = self.db.query(Sans).filter(Sans.id == id).first()
        if sans_db:
            sans_db.delete()
            self.db.commit()
            return True
        return False
from typing import Type

from sqlalchemy.orm import Session

from database.base import session
from database.models.sans import Sans
from repository.base import BaseRepository


class SansRepository(BaseRepository):

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Type[Sans]]:
        sanses: list[Type[Sans]] = self.db.query(Sans).all()
        return sanses

    def get_by_id(self, id: int) -> Type[Sans]:
        sans = self.db.query(Sans).filter(Sans.id == id).first()
        if sans:
            return sans
        return None

    def create(self, item: Sans) -> Sans:
        try:
            sans = item
            self.db.add(item)
            self.db.commit()
            self.db.refresh(item)
            return sans
        except Exception as e:
            self.db.rollback()
            pass

    def update(self, item: Type[Sans]) -> Type[Sans]:
        sans = self.db.query(Sans).filter(Sans.id == item.id).first()
        if sans:
            try:
                sans = item
                self.db.commit()
                self.db.refresh(sans)
                return sans
            except Exception as e:
                self.db.rollback()
                pass
        else:
            pass

    def delete(self, id: int) -> bool:
        sans = self.db.query(Sans).filter(Sans.id == id).first()
        if sans:
            self.db.delete(sans)
            self.db.commit()
            return True
        return False


sans_repository = SansRepository(session)
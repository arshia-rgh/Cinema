from typing import Type

from sqlalchemy.orm import Session

from database import Manager
from repository.base import BaseRepository


class ManagerRepository(BaseRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Type[Manager]]:
        managers = self.db.query(Manager).all()
        return managers

    def get_by_id(self, id: int) -> Type[Manager] | None:
        manager = self.db.query(Manager).filter(Manager.id).first()
        if manager:
            return manager
        return None

    def create(self, item: Type[Manager]) -> Type[Manager]:
        try:
            self.db.add(item)
            self.db.commit()
            self.db.refresh(item)
            return item
        except Exception as e:
            self.db.rollback()

    def update(self, item: Type[Manager]) -> Type[Manager]:
        manager = self.db.query(Manager).filter(Manager.id == item.id).first()
        if manager:
            try:
                manager = item
                self.db.commit()
                self.db.refresh(manager)
                return manager
            except Exception as e:
                self.db.rollback()
                # TODO: raise ManagerUpdateError
        else:
            # TODO: ManagerNotFoundError
            pass

    def delete(self, id: int) -> bool:
        manager = self.db.query(Manager).filter(Manager.id == id).first()
        if manager:
            self.db.delete(manager)
            self.db.commit()
            return True
        return False

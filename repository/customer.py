from typing import Type

from sqlalchemy.orm import Session

from database.base import session
from database import Customer
from repository.base import BaseRepository


class CustomerRepository(BaseRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Type[Customer]]:
        customers = self.db.query(Customer).all()
        return customers

    def get_by_id(self, id: int) -> Type[Customer] | None:
        customer = self.db.query(Customer).filter(Customer.id == id).first()
        if customer:
            return customer
        return None

    def create(self, item: Type[Customer]) -> Type[Customer]:
        try:
            self.db.add(item)
            self.db.commit()
            self.db.refresh(item)
            return item
        except Exception as e:
            # TODO raise UserHasConstraintError
            pass

    def update(self, item: Type[Customer]) -> Type[Customer]:
        customer = self.db.query(Customer).filter(Customer.id == item.id).first()
        if customer:
            try:
                customer = item
                self.db.commit()
                self.db.refresh(customer)
                return customer
            except Exception as e:
                self.db.rollback()
                # TODO:  raise CustomerUpdateError

        else:
            # TODO: raise CustomerNotFoundError
            pass

    def delete(self, id: int) -> bool:
        customer = self.db.query(Customer).filter(Customer.id == id).first()
        if customer:
            self.db.delete(customer)
            self.db.commit()
            return True
        return False


customer_repository = CustomerRepository(session)

from typing import Type

from sqlalchemy.orm import Session

from database import Customer
from database.base import session
from repository.base import BaseRepository
from utils.exceptions import UserHasConstraintError, CustomerUpdateError, CustomerNotFoundError


class CustomerRepository(BaseRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Type[Customer]]:
        customers = self.db.query(Customer).all()
        return customers

    def get_by_id(self, id: int) -> Customer | None:
        customer = self.db.query(Customer).filter(Customer.id == id).first()
        if customer:
            return customer
        return None

    def get_by_user_id(self, user_id: int) -> Customer | None:
        customer = self.db.query(Customer).filter(Customer.user_id == user_id).first()
        if customer:
            return customer
        return None

    def create(self, item: Customer) -> Customer:
        try:
            self.db.add(item)
            self.db.commit()
            self.db.refresh(item)
            return item
        except Exception as e:
            raise UserHasConstraintError(f'user_id={item.user_id}, has customer')

    def update(self, item: Customer) -> Customer:
        customer = self.db.query(Customer).filter(Customer.id == item.id).first()
        if customer:
            try:
                customer = item
                self.db.commit()
                self.db.refresh(customer)
                return customer
            except Exception as e:
                self.db.rollback()
                raise CustomerUpdateError(f'customer_id={customer.id}, update failed')

        else:
            raise CustomerNotFoundError(f'customer_id={item.id} not found')

    def delete(self, id: int) -> bool:
        customer = self.db.query(Customer).filter(Customer.id == id).first()
        if customer:
            self.db.delete(customer)
            self.db.commit()
            return True
        return False


customer_repository = CustomerRepository(session)

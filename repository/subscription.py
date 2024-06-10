from sqlalchemy.orm import Session
from typing import Type

from database.base import session
from repository.base import BaseRepository
from database.models.subscription import Subscription, MyEnum


class SubscriptionRepository(BaseRepository):
    """
    A repository for managing Subscription entities in the database.

    Attributes:
        db (Session): The database session to use for queries.

    Methods:
        get_all(): Returns all Subscription entities from the database.
        get_by_id(id: int): Returns the Subscription entity with the given id.
        get_by_customer_id(customer_id: int): Returns the Subscription entity with the given customer id.
        get_all_paid_subscriptions(): Returns all paid Subscription entities (silver and gold) from the database.
        get_all_free_subscriptions(): Returns all free Subscription entities (bronze) from the database.
        create(item: Subscription): Adds a new Subscription entity to the database.
        update(item: Subscription): Updates an existing Subscription entity in the database.
        delete(id: int): Deletes the Subscription entity with the given id from the database.
    """
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Type[Subscription]] | None:
        subscriptions = self.db.query(Subscription).all()
        return subscriptions

    def get_by_id(self, id: int) -> Type[Subscription] | None:
        subscription = self.db.query(Subscription).filter(Subscription.id == id).first()
        if subscription:
            return subscription
        return None

    def get_by_customer_id(self, customer_id: int) -> list[Type[Subscription]] | None:
        subscription = self.db.query(Subscription).filter(Subscription.customer_id == customer_id).first()
        return subscription

    def get_all_paid_subscriptions(self) -> list[Type[Subscription]] | None:
        subscriptions = self.db.query(Subscription).filter(Subscription.type.in_([MyEnum.silver, MyEnum.gold])).all()
        return subscriptions

    def get_all_free_subscriptions(self) -> list[Type[Subscription]] | None:
        subscriptions = self.db.query(Subscription).filter(Subscription.type == MyEnum.bronze).all()
        return subscriptions

    def create(self, item: Subscription) -> Subscription:  # TODO should handle exceptions later
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def update(self, item: Type[Subscription]) -> Type[Subscription] | None:  # TODO should handle exceptions later
        subscription = self.db.query(Subscription).filter(Subscription.id == item.id).first()
        if subscription:
            subscription = item
            self.db.commit()
            self.db.refresh(subscription)
            return subscription
        return None

    def delete(self, id: int) -> bool:
        subscription = self.db.query(Subscription).filter(Subscription.id == id).first()
        if subscription:
            self.db.delete(subscription)
            self.db.commit()
            return True
        return False


subscription_repository = SubscriptionRepository(session)

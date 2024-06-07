from dataclasses import dataclass


@dataclass
class BankAccountInDB:
    customer_id: int
    card_number: str
    password: str
    cvv2: str
    balance: float


@dataclass
class BankAccountOutput:
    id: int
    customer_id: int
    card_number: str
    password: str
    cvv2: str
    balance: float


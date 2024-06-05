from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserInDB:
    username: str
    password: str
    email: str
    phone: str | None
    last_login: datetime | None


@dataclass
class UserOutput:
    id: int
    username: str
    password: str
    email: str
    phone: str | None
    last_login: datetime | None

from datetime import datetime
from dataclasses import dataclass


@dataclass
class User:
    name: str
    login: str
    password: str
    id: int = None

@dataclass
class Token:
    user_id: int
    token: str
    expired: datetime
    id: int = None
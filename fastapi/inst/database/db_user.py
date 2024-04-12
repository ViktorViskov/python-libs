from sqlalchemy.orm import Session

from .schemes import UserDb
from database import hash
from models.user import UserCreate

def create(db: Session, user: UserCreate) -> UserDb:
    db_user = UserDb()
    db_user.username = user.username
    db_user.email = user.email
    db_user.password = hash.hash_password(user.password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all(db: Session) -> list[UserDb]:
    return db.query(UserDb).all()

def get(db: Session, id: int) -> UserDb | None:
    return db.query(UserDb).where(UserDb.id == id).first()

def get_by_username(db: Session, username: str) -> UserDb | None:
    return db.query(UserDb).where(UserDb.username == username).first()
from datetime import datetime
from dataclasses import dataclass

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import and_
from sqlalchemy import text
from sqlalchemy import Select
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.functions import count
from sqlalchemy import Row 

from auth_schemes import User
from auth_schemes import Token


class AuthDB:
    def __init__(self) -> None:
        # create engine
        self.engine = create_engine('sqlite:///sqlite3.db', echo=False)

        # describe db structure
        self._describe_db()

    # Init ORM
    def _describe_db(self) -> None:
        # create variable with metadata for db
        self.metadata = MetaData()

        # table for user
        self.users = Table(
            "users", 
            self.metadata, 
            Column("id", Integer(), primary_key=True, autoincrement=True), 
            Column("name", String(64)), 
            Column("login", String(64), unique=True), 
            Column("password", String(64)),
            Column("created", DateTime(), default=current_timestamp()))
        
        # table for user tokens
        self.tokens = Table(
            "tokens", 
            self.metadata, 
            Column("id", Integer(), primary_key=True, autoincrement=True), 
            Column("user_id", Integer(), ForeignKey('users.id')),
            Column("expired", DateTime()),
            Column("token", String(256)))
        
    def create_db(self) -> None:
        self.connection = self.engine.connect()
        self.metadata.create_all(self.engine)
        self.connection.close()

    def _parse_user(self, row: Row | None) -> User | None:
        result = None
        if row:
            result = User(
                id=row[0],
                name=row[1],
                login=row[2],
                password=row[3]
            )
        return result
    
    def _parse_token(self, row: Row | None) -> Token | None:
        result = None
        if row:
            result = Token(
                id=row[0],
                user_id=row[1],
                expired=row[2],
                token=row[3]
            )
        return result

    # Users
    def add_user(self, user: User) -> int:
        connection = self.engine.connect()

        query = self.users.insert().values(
            name=user.name,
            login=user.login,
            password=user.password)
        
        record_id = connection.execute(query).inserted_primary_key
        connection.commit()
        connection.close()
        return record_id[0]

    def get_user_by_login(self, login: str) -> User | None:
        connection = self.engine.connect()

        query = self.users.select().where(self.users.columns.login == login)

        result = connection.execute(query).fetchone()
        connection.close()
        return self._parse_user(result)
    
    def get_user_by_login_and_password(self, login: str, password: str) -> User | None:
        connection = self.engine.connect()

        query = self.users.select().where(and_(
            self.users.columns.login == login, 
            self.users.columns.password == password))
        
        result = connection.execute(query).fetchone()
        connection.close()
        return self._parse_user(result)

    def get_users_all(self) -> list[User]:
        connection = self.engine.connect()

        query = self.users.select()

        result = connection.execute(query).fetchall()
        connection.close()
        return [self._parse_user(r) for r in result]
    
    def user_update(self, user: User) -> None:
        connection = self.engine.connect()

        query = self.users.update().values(
            name=user.name, 
            login=user.login, 
            password=user.password
        ).where(
            self.users.columns.id == user.id)
        
        connection.execute(query)
        connection.commit()
        connection.close()

    def user_delete(self, user_id: int) -> None:
        connection = self.engine.connect()

        query = self.users.delete().where(self.users.columns.id == user_id)

        connection.execute(query)
        connection.commit()
        connection.close()

    # Tokens
    def add_token(self, token: Token) -> int:
        connection = self.engine.connect()

        query = self.tokens.insert().values(
            user_id=token.user_id,
            expired=token.expired,
            token=token.token)
        
        record_id = connection.execute(query).inserted_primary_key
        connection.commit()
        connection.close()
        return record_id[0]

    def get_user_by_token(self, token_hash: str) -> User:
        connection = self.engine.connect()

        query = self.users.select().where(self.tokens.columns.token == token_hash)

        query = self.users.select().join(self.tokens, self.tokens.columns.user_id == self.users.columns.id).where(
            self.tokens.columns.token == token_hash
        )

        result = connection.execute(query).fetchone()
        connection.close()
        return self._parse_user(result)
    
    def get_token_by_id(self, id: int) -> Token:
        connection = self.engine.connect()
        query = self.tokens.select().where(self.tokens.columns.id == id)

        result = connection.execute(query).fetchone()
        connection.close()
        return self._parse_token(result)

    def get_token(self, token_hash: str) -> Token:
        connection = self.engine.connect()
        query = self.tokens.select().where(self.tokens.columns.token == token_hash)

        result = connection.execute(query).fetchone()
        connection.close()
        return self._parse_token(result)

    def get_tokens_all(self) -> list[Token]:
        connection = self.engine.connect()

        query = self.tokens.select()

        result = connection.execute(query).fetchall()
        connection.close()
        return [self._parse_token(r) for r in result]

    def get_user_tokens(self, user: User) -> list[Token]:
        connection = self.engine.connect()

        query = self.tokens.select().where(
            self.tokens.columns.user_id == user.id
        )

        result = connection.execute(query).fetchall()
        connection.close()
        return [self._parse_token(r) for r in result]

    def token_delete(self, token_id: int) -> None:
        connection = self.engine.connect()

        query = self.tokens.delete().where(self.tokens.columns.id == token_id)

        connection.execute(query)
        connection.commit()
        connection.close()
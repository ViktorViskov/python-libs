from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import text
from sqlalchemy import Select

from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.functions import count


class Controller:
    def __init__(self) -> None:
        # create engine
        self.engine = create_engine('sqlite:///sqlite3.db', echo=True)

        # describe db structure
        self._describe_db()

        # create db
        # self._create_db()

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
        
        # table for user address
        self.addresses = Table(
            "addresses", 
            self.metadata, 
            Column("id", Integer(), primary_key=True, autoincrement=True), 
            Column("user_id", Integer(), ForeignKey('users.id')),
            Column("address", String(64)))
    

    # create table from metadata
    def _create_db(self) -> None:
        # open connection
        self.connection = self.engine.connect()

        # request to create tables
        self.metadata.create_all(self.engine)

        # close connection
        self.connection.close()

    # Create user in db
    def add_user(self, name: str, login: str, password:str) -> None:
        # open connection
        connection = self.engine.connect()

        # preprocess login
        login = login.lower()

        # check for login is available and create
        data = connection.execute(self.users.select().where(self.users.columns.login == login)).fetchone()
        if data == None:
            connection.execute(self.users.insert().values(name=name,login=login,password=password))
            connection.commit()

        connection.close()

    def get_users_all(self) -> None:
        # preprocess login and open connection
        connection = self.engine.connect()
        query = self.users.select()
        result = connection.execute(query).fetchall()
        print(result)
        connection.close()
    
    def get_user_by_id(self, user_id: int) -> None:
        # preprocess login and open connection
        connection = self.engine.connect()
        query = self.users.select().where(self.users.columns.id == user_id)
        result = connection.execute(query).fetchone()
        print(result)
        connection.close()

    def user_update(self, user_id: int, name: str, login: str, password: str) -> None:
        connection = self.engine.connect()
        query = self.users.update().values(name=name, login=login, password=password).where(self.users.columns.id == user_id)
        connection.execute(query)
        connection.commit()
        connection.close()

    def user_delete(self, user_id: int) -> None:
        connection = self.engine.connect()
        query = self.users.delete().where(self.users.columns.id == user_id)
        connection.execute(query)
        connection.commit()
        connection.close()

    def add_address(self, user_id: int, address: str) -> None:
        # preprocess login and open connection
        connection = self.engine.connect()

        # check for user exist
        user = connection.execute(self.users.select().where(self.users.columns.id == user_id)).fetchone()
        if not user:
            print("User not exist")
            return
        
        connection.execute(self.addresses.insert().values(user_id=user_id, address=address))
        connection.commit()
        connection.close()
    
    def get_addresses_all(self) -> None:
        connection = self.engine.connect()
        query = self.addresses.select()
        result = connection.execute(query).fetchall()
        print(result)
        connection.close()
    

    # inner join example
    def get_address_by_user_login(self, user_login: str) -> None:
        connection = self.engine.connect()
        query = self.addresses.select().join(self.users, self.addresses.c.id == self.users.c.id).where(self.users.columns.login == user_login)
        result = connection.execute(query).fetchone()
        print(result)
        connection.close()

    def address_delete(self, address_id: int) -> None:
        connection = self.engine.connect()
        query = self.addresses.delete().where(self.addresses.columns.id == address_id)
        connection.execute(query)
        connection.commit()
        connection.close()

    def address_count(self) -> int:
        con = self.engine.connect()

        query = self.users.select().order_by(self.users.columns.id.desc()).limit(5)
        result = con.execute(query).fetchall()

        return list(reversed(result))
        # return result
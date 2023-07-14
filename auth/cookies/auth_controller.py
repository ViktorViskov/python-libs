from datetime import datetime
from hashlib import sha256

from auth_db import AuthDB
from auth_schemes import User
from auth_schemes import Token


class AuthController:
    HASH_SALT = "THis is Salt"
    SHORT_SESSION = 3600 * 24 * 7
    LONG_SESSION = 3600 * 24 * 31

    def __init__(self) -> None:
        self.users_db = AuthDB()

    def _format_login(self, login: str) -> str:
        return login.strip().replace(" ", "").lower()
    
    def _hash_password(self, password: str) -> str:
        to_hash = password + self.HASH_SALT
        return sha256(to_hash.encode()).hexdigest()
    
    def _generate_token(self, login: str, now: datetime) -> str:
        timestamp = now.timestamp()
        to_hash = login + str(timestamp) + self.HASH_SALT
        return sha256(to_hash.encode()).hexdigest()
    
    def _delete_expired_tokens(self, tokens: list[Token]) -> None:
        now = datetime.now()
        for t in tokens:
            if t.expired < now:
                self.users_db.token_delete(t.id)

    def register_user(self, name: str, login: str, password: str, password_conf: str) -> str:
        login_lower = self._format_login(login)
        password_hashed = self._hash_password(password)
        password_same = password == password_conf

        if not login_lower:
            return "Login can not be empty"
        
        if not password_same:
            return "Password must be same"
        
        exist_user = self.users_db.get_user_by_login(login_lower)
        if exist_user:
            return f"User {login} exist"
        
        user = User(name, login_lower, password_hashed)
        self.users_db.add_user(user)

        return "Registered"

    def login_user(self, login: str, password: str, is_long_session: bool = False) -> Token | None:
        now =  datetime.now()
        login_lower = self._format_login(login)
        password_hash = self._hash_password(password)
        user = self.users_db.get_user_by_login_and_password(login_lower, password_hash)

        if not user:
            return None
        
        self._delete_expired_tokens(self.users_db.get_user_tokens(user))

        session_size = self.LONG_SESSION if is_long_session else self.SHORT_SESSION 
        exp = datetime.fromtimestamp(now.timestamp() + session_size)
        token = self._generate_token(user.login, now)
        session_token = Token(
            user.id,
            token,
            exp)
        token_id = self.users_db.add_token(session_token)

        return self.users_db.get_token_by_id(token_id)

    def logout_user(self, token_hash: str) -> None:
        token = self.users_db.get_token(token_hash)
        if token:
            self.users_db.token_delete(token.id)       

    def check_token(self, token_hash: str) -> bool:
        now = datetime.now()
        token = self.users_db.get_token(token_hash)

        if not token:
            return False

        if token.expired < now:
            self.users_db.token_delete(token.id)
            return False

        return True
        
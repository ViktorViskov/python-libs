from passlib.context import CryptContext


def hash_password(password):
    crypt_context = CryptContext("bcrypt")
    return crypt_context.hash(password)

def verify_password(password, hash):
    crypt_context = CryptContext("bcrypt")
    return crypt_context.verify(password, hash)
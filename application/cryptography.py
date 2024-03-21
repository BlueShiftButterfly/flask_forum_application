import bcrypt

def hash_password(password: str, gensalt_amount: int = 12) -> str:
    pw_bytes = password.encode()
    pw_salt = bcrypt.gensalt(gensalt_amount)
    return bcrypt.hashpw(pw_bytes, pw_salt).decode()

def check_password(password: str, password_hash: str) -> bool:
    return bcrypt.checkpw(password.encode(), password_hash.encode())

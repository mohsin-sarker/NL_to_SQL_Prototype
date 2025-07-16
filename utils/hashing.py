import bcrypt

# Create to hash password and verify the hashed password.
def hash_password(password: str):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed.decode()


def verify_password(password: str, hashed: str):
    return bcrypt.checkpw(password.encode(), hashed.encode())


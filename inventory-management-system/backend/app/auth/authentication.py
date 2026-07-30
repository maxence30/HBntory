import bcrypt

from app.models.user import User


def hash_password(password):
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


def verify_password(password, password_hash):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        password_hash.encode("utf-8")
    )


def authenticate_user(session, username, password):
    user = (
        session.query(User)
        .filter(User.username == username)
        .first()
    )

    if user is None:
        return None

    if user.is_deleted:
        return None

    if not verify_password(password, user.password_hash):
        return None

    return user
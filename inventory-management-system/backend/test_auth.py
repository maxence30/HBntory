from app.database import SessionLocal
from app.auth.authentication import authenticate_user


session = SessionLocal()


user = authenticate_user(
    session,
    "admin",
    "admin123"
)


if user:
    print(
        "Login successful:",
        user.username,
        user.role
    )
else:
    print("Login failed")


session.close()
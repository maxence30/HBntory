from app.database import Base, engine, SessionLocal
from app.models import User, Branch, Stock

import bcrypt


# Create database tables
Base.metadata.create_all(bind=engine)


session = SessionLocal()


def hash_password(password):
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


# Create branches
dijon = Branch(name="Dijon")
paris = Branch(name="Paris")

session.add(dijon)
session.add(paris)

session.commit()


# Create admin user
admin = User(
    username="admin",
    password_hash=hash_password("admin123"),
    role="admin",
    branch_id=None
)

# Create common users
user1 = User(
    username="employee_dijon",
    password_hash=hash_password("password123"),
    role="common",
    branch_id=dijon.id
)

user2 = User(
    username="employee_paris",
    password_hash=hash_password("password123"),
    role="common",
    branch_id=paris.id
)


session.add(admin)
session.add(user1)
session.add(user2)


# Create sample stock
stock1 = Stock(
    branch_id=dijon.id,
    product_id=1,
    quantity=10
)

stock2 = Stock(
    branch_id=paris.id,
    product_id=2,
    quantity=5
)


session.add(stock1)
session.add(stock2)


session.commit()

print("Database initialized successfully")

session.close()
from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

from app.database import Base


class Stock(Base):
    __tablename__ = "stocks"

    __table_args__ = (
        CheckConstraint(
            "quantity >= 0",
            name="stock_quantity_non_negative"
        ),
    )

    id = Column(
        Integer,
        primary_key=True
    )

    branch_id = Column(
        Integer,
        ForeignKey("branches.id"),
        nullable=False
    )

    product_id = Column(
        Integer,
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False,
        default=0
    )

    branch = relationship(
        "Branch",
        back_populates="stocks"
    )
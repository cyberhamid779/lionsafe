from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    org_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    email = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    department = Column(String(255))
    is_admin = Column(Boolean, default=False)
    hashed_password = Column(String(255))  # only for admin users

    clicks = relationship("Click", back_populates="user")

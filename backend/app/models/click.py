from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.models.base import Base


class Click(Base):
    __tablename__ = "clicks"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    token = Column(String(64), unique=True, nullable=False)
    clicked = Column(Boolean, default=False)
    clicked_at = Column(DateTime)
    trained = Column(Boolean, default=False)
    ip_hash = Column(String(64))

    user = relationship("User", back_populates="clicks")
    campaign = relationship("Campaign", back_populates="clicks")

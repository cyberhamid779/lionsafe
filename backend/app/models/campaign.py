from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from app.models.base import Base


class CampaignStatus(str, enum.Enum):
    draft = "draft"
    active = "active"
    completed = "completed"


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True)
    org_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    template_id = Column(Integer, ForeignKey("templates.id"), nullable=False)
    name = Column(String(255), nullable=False)
    status = Column(Enum(CampaignStatus), default=CampaignStatus.draft)

    clicks = relationship("Click", back_populates="campaign")
    template = relationship("Template")

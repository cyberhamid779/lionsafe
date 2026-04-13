from sqlalchemy import Column, Integer, String, Text
from app.models.base import Base


class Template(Base):
    __tablename__ = "templates"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=False)
    body_html = Column(Text, nullable=False)
    training_html = Column(Text, nullable=False)  # shown after click
    category = Column(String(100))  # e.g. "it_support", "hr", "finance"

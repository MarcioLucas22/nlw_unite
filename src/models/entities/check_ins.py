from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from src.models.entities.attendees import Attendees

class CheckIns(Base):
    __tablename__ = "check_ins"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    attendeeId = Column(String, ForeignKey(Attendees.id))

    def __repr__(self):
        return f"Check-ins [attendeeId={self.attendeeId}]"

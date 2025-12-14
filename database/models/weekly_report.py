from sqlalchemy import Column, BigInteger, DateTime
from datetime import datetime
from database.models.base import Base



class WeeklyReport(Base):
    __tablename__ = "weekly_reports"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

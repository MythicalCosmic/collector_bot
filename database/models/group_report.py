from sqlalchemy import Column, BigInteger, String, DateTime
from datetime import datetime
from database.models.base import Base
from sqlalchemy import ForeignKey


class GroupReport(Base):
    __tablename__ = "group_reports"

    id = Column(BigInteger, primary_key=True)
    weekly_report_id = Column(
        BigInteger,
        ForeignKey("weekly_reports.id"),
        nullable=False,
    )

    group_name = Column(String, nullable=False)
    group_time = Column(String, nullable=False)
    student_count = Column(BigInteger, nullable=False)
    student_present = Column(BigInteger, nullable=False)
    student_paid = Column(BigInteger, nullable=False)
    exam_day = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
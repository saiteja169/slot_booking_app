from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base

class Slot(Base):
    __tablename__ = "slots"

    id = Column(Integer, primary_key=True, index=True)
    slot_time = Column(String(50), nullable=False)
    is_booked = Column(Boolean, default=False)

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    slot_id = Column(Integer, ForeignKey("slots.id"))
    user_name = Column(String(100), nullable=False)
    user_email = Column(String(100), nullable=False)
    booked_at = Column(DateTime, server_default=func.now())
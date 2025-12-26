from sqlalchemy import Column, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from stayops.infrastructure.db.base import Base
from stayops.domain.aggregates.base import AuditableMixin
import enum

class BookingPlatform(enum.Enum):
    AIRBNB = "AIRBNB"
    BOOKING = "BOOKING"

class BookingStatus(enum.Enum):
    SCHEDULED = "SCHEDULED"
    CHECKED_OUT = "CHECKED_OUT"
    READY = "READY"

class Booking(Base, AuditableMixin):
    __tablename__ = "bookings"

    property_id = Column(UUID(as_uuid=True), nullable=False)
    platform = Column(Enum(BookingPlatform), nullable=False)

    check_in = Column(DateTime, nullable=False)
    check_out = Column(DateTime, nullable=False)
    actual_checkout = Column(DateTime)

    status = Column(Enum(BookingStatus), nullable=False)

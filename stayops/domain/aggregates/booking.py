# stayops/domain/aggregates/booking.py
import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID

from stayops.extensions import db
from stayops.domain.aggregates.base import AuditableMixin
from stayops.domain.enums import BookingStatus, BookingPlatform


class Booking(db.Model, AuditableMixin):
    __tablename__ = "bookings"

    property_id = Column(UUID(as_uuid=True), nullable=False)

    platform = Column(
        Enum(BookingPlatform, name="bookingplatform"),
        nullable=False
    )

    check_in = Column(DateTime, nullable=False)
    check_out = Column(DateTime, nullable=False)
    actual_checkout = Column(DateTime, nullable=True)

    status = Column(
        Enum(BookingStatus, name="bookingstatus"),
        nullable=False,
        default=BookingStatus.SCHEDULED
    )

    # ---- Domain invariants ----
    @staticmethod
    def create(
        *,
        tenant_id: uuid.UUID,
        property_id: uuid.UUID,
        platform: BookingPlatform,
        check_in: datetime,
        check_out: datetime,
        actor_id: uuid.UUID
    ) -> "Booking":

        if check_out <= check_in:
            raise ValueError("check_out must be after check_in")

        return Booking(
            tenant_id=tenant_id,
            property_id=property_id,
            platform=platform,
            check_in=check_in,
            check_out=check_out,
            status=BookingStatus.SCHEDULED,
            created_by=actor_id
        )

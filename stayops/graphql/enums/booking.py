import graphene
from stayops.domain.enums import BookingStatus, BookingPlatform


BookingStatusEnum = graphene.Enum.from_enum(
    BookingStatus,
    description="Lifecycle state of a booking"
)

BookingPlatformEnum = graphene.Enum.from_enum(
    BookingPlatform,
    description="Platform through which the booking was created"
)

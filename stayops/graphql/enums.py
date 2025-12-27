import graphene
from stayops.domain.enums import BookingStatus, BookingPlatform


class BookingStatusEnum(graphene.Enum):
    PENDING = BookingStatus.PENDING.value
    CONFIRMED = BookingStatus.CONFIRMED.value
    CANCELLED = BookingStatus.CANCELLED.value
    COMPLETED = BookingStatus.COMPLETED.value


class BookingPlatformEnum(graphene.Enum):
    DIRECT = BookingPlatform.DIRECT.value
    AIRBNB = BookingPlatform.AIRBNB.value
    BOOKING_COM = BookingPlatform.BOOKING_COM.value
    EXPEDIA = BookingPlatform.EXPEDIA.value
    OTHER = BookingPlatform.OTHER.value

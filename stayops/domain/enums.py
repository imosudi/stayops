# stayops/domain/enums.py
from enum import Enum
from enum import Enum


class BookingStatus(str, Enum):
    SCHEDULED = "SCHEDULED"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"

"""
class BookingStatus(str, Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED" """


class BookingPlatform(str, Enum):
    DIRECT = "DIRECT"
    AIRBNB = "AIRBNB"
    BOOKING_COM = "BOOKING_COM"
    EXPEDIA = "EXPEDIA"
    OTHER = "OTHER"

import graphene
from stayops.domain.aggregates.booking import Booking
from stayops.graphql.types.base import AuditableObjectType
from stayops.graphql.interfaces import AuditableInterface


class BookingPlatformEnum(graphene.Enum):
    AIRBNB = "AIRBNB"
    BOOKING = "BOOKING"

class BookingStatusEnum(graphene.Enum):
    SCHEDULED = "SCHEDULED"
    CHECKED_OUT = "CHECKED_OUT"
    READY = "READY"

class BookingType(AuditableObjectType):
    class Meta:
        model = Booking
        load_instance = True

"""class BookingType(AuditableObjectType):
    class Meta:
        model = Booking
        interfaces = (AuditableInterface, graphene.relay.Node)"""


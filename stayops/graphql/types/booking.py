import graphene
from stayops.graphql.enums.booking import (
    BookingStatusEnum,
    BookingPlatformEnum,
)

class CreateBookingInput(graphene.InputObjectType):
    """
    Input contract for creating a booking.
    Domain invariants are enforced in the mutation, not here.
    """

    tenant_id = graphene.UUID(required=True)
    property_id = graphene.UUID(required=True)

    platform = BookingPlatformEnum(required=True)

    check_in = graphene.DateTime(required=True)
    check_out = graphene.DateTime(required=True)
    
class BookingType(graphene.ObjectType):
    id = graphene.UUID()
    status = BookingStatusEnum(required=True)
    platform = BookingPlatformEnum(required=True)

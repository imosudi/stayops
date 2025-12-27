import graphene
from datetime import datetime
from flask import g

from stayops.extensions import db
from stayops.domain.aggregates.booking import Booking
from stayops.graphql.types.booking import BookingType, CreateBookingInput


class CreateBooking(graphene.Mutation):
    """
    Creates a new booking aggregate.
    """

    booking = graphene.Field(BookingType)

    class Arguments:
        input = CreateBookingInput(required=True)

    def mutate(self, info, input: CreateBookingInput):
        # In a real system these come from auth context
        actor_id = getattr(g, "user_id", None)
        if actor_id is None:
            raise Exception("Unauthenticated")

        booking = Booking(
            tenant_id=input.tenant_id,
            property_id=input.property_id,
            platform=input.platform,   # enum value is correct
            check_in=input.check_in,
            check_out=input.check_out,
            created_by=actor_id,
            created_at=datetime.utcnow(),
        )

        db.session.add(booking)
        db.session.commit()

        return CreateBooking(booking=booking)

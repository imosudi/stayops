import graphene
from stayops.graphql.mutations.booking import CreateBooking
from stayops.graphql.types.booking import BookingType


class Mutation(graphene.ObjectType):
    create_booking = CreateBooking.Field()


class Query(graphene.ObjectType):
    booking = graphene.Field(
        BookingType,
        id=graphene.UUID(required=True)
    )

    def resolve_booking(self, info, id):
        from stayops.domain.aggregates.booking import Booking
        return Booking.query.get(id)


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)

# stayops/graphql/queries.py
import graphene
from stayops import db
from stayops.domain.aggregates.booking import Booking
from stayops.graphql.types.booking import BookingType

class Query(graphene.ObjectType):
    health = graphene.NonNull(graphene.String)
    booking = graphene.Field(
        BookingType,
        id=graphene.UUID(required=True)
    )
    bookings = graphene.List(BookingType)

    def resolve_health(root, info):
        return "OK"

    def resolve_booking(root, info, id):
        return db.session.get(Booking, id)

    def resolve_bookings(root, info):
        return db.session.query(Booking).filter_by(is_deleted=False).all()

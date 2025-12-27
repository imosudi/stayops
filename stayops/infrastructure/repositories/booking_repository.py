from stayops.domain.aggregates.booking import Booking


class BookingRepository:
    def __init__(self, session):
        self.session = session

    def add(self, booking: Booking) -> Booking:
        self.session.add(booking)
        return booking

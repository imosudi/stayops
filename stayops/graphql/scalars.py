import graphene
import uuid
from datetime import datetime

class UUIDScalar(graphene.Scalar):
    """UUID scalar"""

    @staticmethod
    def serialize(value):
        return str(value)

    @staticmethod
    def parse_value(value):
        return uuid.UUID(value)

    @staticmethod
    def parse_literal(node):
        return uuid.UUID(node.value)


class DateTimeScalar(graphene.Scalar):
    """ISO-8601 DateTime"""

    @staticmethod
    def serialize(value):
        return value.isoformat() if value else None

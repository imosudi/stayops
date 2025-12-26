from graphene_sqlalchemy import SQLAlchemyObjectType
from stayops.graphql.interfaces import AuditableInterface

class AuditableObjectType(SQLAlchemyObjectType):
    """
    Base GraphQL type for all auditable aggregates.

    IMPORTANT:
    - Must ONLY declare `abstract = True`
    - Interfaces are added in concrete subclasses
    """

    class Meta:
        abstract = True
        #interfaces = (AuditableInterface,)



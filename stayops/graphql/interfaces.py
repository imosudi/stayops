import graphene
from stayops.graphql.scalars import UUIDScalar, DateTimeScalar

class AuditableInterface(graphene.Interface):
    id = graphene.ID(required=True)
    tenant_id = UUIDScalar(required=True)

    created_at = DateTimeScalar(required=True)
    created_by = UUIDScalar(required=True)

    updated_at = DateTimeScalar()
    updated_by = UUIDScalar()

    deleted_at = DateTimeScalar()
    deleted_by = UUIDScalar()

    is_deleted = graphene.Boolean(required=True)

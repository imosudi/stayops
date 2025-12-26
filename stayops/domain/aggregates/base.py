# stayops/domain/aggregates/base.py
import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID

class AuditableMixin:
    """
    Cross-cutting audit + soft-delete concerns.
    Enforced at the domain level, not GraphQL.
    """

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    tenant_id = Column(UUID(as_uuid=True), nullable=False)

    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    created_by = Column(UUID(as_uuid=True), nullable=False)

    updated_at = Column(DateTime, nullable=True)
    updated_by = Column(UUID(as_uuid=True), nullable=True)

    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(UUID(as_uuid=True), nullable=True)

    is_deleted = Column(Boolean, nullable=False, default=False)

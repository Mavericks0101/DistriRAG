from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class TenantContext:
    tenant_id: str


@dataclass
class Document:
    id: str
    tenant_context: TenantContext
    collection_id: str
    active_version_id: Optional[str] = None
    deleted_at: Optional[datetime] = None

    @property
    def is_active(self) -> bool:
        return self.active_version_id is not None and self.deleted_at is None

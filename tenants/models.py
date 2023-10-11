from django_tenants.models import TenantMixin, DomainMixin
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField

# Create your models here.


class Tenant(TenantMixin):
    history = AuditlogHistoryField()
    auto_create_schema = True


class Domain(DomainMixin):
    history = AuditlogHistoryField()
    pass

auditlog.register(Tenant)
auditlog.register(Domain)
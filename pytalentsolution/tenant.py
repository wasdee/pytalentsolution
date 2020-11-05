from typing import Optional

from google.cloud import talent
from pydantic import constr, PrivateAttr

from pytalentsolution import settings
from pytalentsolution.cts import CTSModel

client_tenant = talent.TenantServiceClient()


# TODO: this is absent in `.venv/Lib/site-packages/google/cloud/talent_v4/types/tenant.py`
# class DataUsageType(AutoName):
#     """
#     https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants#DataUsageType
#     """
#     DATA_USAGE_TYPE_UNSPECIFIED = auto()
#     AGGREGATED = auto()
#     ISOLATED = auto()

class TenantInCreate(CTSModel):
    """
        https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants
    """

    external_id: constr(max_length=255)

    # TODO: this is absent in `.venv/Lib/site-packages/google/cloud/talent_v4/types/tenant.py`
    # usage_type: Optional[DataUsageType] = None
    # keyword_searchable_profile_custom_attributes: Optional[List[str]] = None


class Tenant(TenantInCreate):
    _parent = PrivateAttr(f"projects/{settings.project_id}")

    name: Optional[str] = None  # project/project_id/tenant/tenant_id, You will receive it when tenant has been created.

    def create(self):
        tenant = talent.Tenant(**self.dict())
        response = client_tenant.create_tenant(parent=self._parent, tenant=tenant)
        self.name = response.name

    @classmethod
    def get(cls, name):
        response = client_tenant.get_tenant(name=name)
        return cls.from_orm(response)

    def update(self):
        tenant = talent.Tenant(**self.dict())
        _ = client_tenant.update_tenant(tenant=tenant)

    def delete(self):
        client_tenant.delete_tenant(name=self.name)
        self.name = None

    @classmethod
    def list(cls):
        return [
            cls(**cls.proto_to_dict(response))
            for response
            in client_tenant.list_tenants(parent=f"projects/{settings.project_id}")
        ]


__all__ = ["Tenant"]

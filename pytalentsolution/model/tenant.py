from enum import auto
from typing import Optional, List

from pydantic import BaseModel

from pytalentsolution.model.company import AutoName


class DataUsageType(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants#DataUsageType
    """
    DATA_USAGE_TYPE_UNSPECIFIED = auto()
    AGGREGATED = auto()
    ISOLATED = auto()


class Tenant(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants
    """
    name: Optional[str] #  project/project_id/tenant/tenant_id, You will receive it when tenant has been created.
    external_id: str
    usage_type: Optional[DataUsageType]
    keyword_searchable_profile_custom_attributes: Optional[List[str]]



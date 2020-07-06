from enum import auto
from typing import Optional, List

from pydantic import BaseModel

from pytalentsolution.company import AutoName


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
    name: str
    externalId: str
    usageType: Optional[DataUsageType]
    keywordSearchableProfileCustomAttributes: Optional[List[str]]
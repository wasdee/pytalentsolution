from enum import auto
from typing import List, Optional

from pydantic import BaseModel

from pytalentsolution.enum_util import AutoName


class LatLng(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/Location#LatLng
    """
    latitude: int
    longitude: int


class PostalAddress(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/PostalAddress
    """
    revision: Optional[int]
    regionCode: str
    languageCode: Optional[str]
    postalCode: Optional[str]
    sortingCode: Optional[str]
    administrativeArea: Optional[str]
    locality: Optional[str]
    sublocality: Optional[str]
    addressLines: Optional[List[str]]
    recipients: Optional[List[str]]
    organization: Optional[str]


class LocationType(AutoName):
    LOCATION_TYPE_UNSPECIFIED = auto()
    COUNTRY = auto()
    ADMINISTRATIVE_AREA = auto()
    SUB_ADMINISTRATIVE_AREA = auto()
    LOCALITY = auto()
    POSTAL_CODE = auto()
    SUB_LOCALITY = auto()
    SUB_LOCALITY_1 = auto()
    SUB_LOCALITY_2 = auto()
    NEIGHBORHOOD = auto()
    STREET_ADDRESS = auto()


class Location(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/Location
    """
    locationType: Optional[LocationType]
    postalAddress: Optional[PostalAddress]
    latLng: Optional[LatLng]
    radiusMiles: Optional[int]


class DerivedInfo(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.companies#derivedinfo
    """
    headquartersLocation: Optional[Location]


class CompanySize(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.companies#companysize
    """
    COMPANY_SIZE_UNSPECIFIED = auto()
    MINI = auto()
    SMALL = auto()
    SMEDIUM = auto()
    MEDIUM = auto()
    BIG = auto()
    BIGGER = auto()
    GIANT = auto()


class Company(BaseModel):
    name: str
    displayName: str
    externalId: str
    size: Optional[CompanySize]
    headquartersAddress: Optional[str]
    hiringAgency: Optional[bool]
    eeoText: Optional[str]
    websiteUri: Optional[str]
    careerSiteUri: Optional[str]
    imageUri: Optional[str]
    keywordSearchableJobCustomAttributes: Optional[List[str]]

    # output
    derivedInfo: Optional[DerivedInfo]
    suspended: Optional[bool]

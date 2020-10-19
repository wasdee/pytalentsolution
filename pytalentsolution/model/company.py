from enum import auto
from typing import List, Optional

from pydantic import BaseModel

from pytalentsolution.model.enum_util import AutoName


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
    region_code: str
    language_code: Optional[str]
    postal_code: Optional[str]
    sorting_code: Optional[str]
    administrative_area: Optional[str]
    locality: Optional[str]
    sublocality: Optional[str]
    address_lines: Optional[List[str]]
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
    location_type: Optional[LocationType]
    postal_address: Optional[PostalAddress]
    latLng: Optional[LatLng]
    radius_miles: Optional[int]


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
    name: Optional[str]
    display_name: str
    external_id: str
    size: Optional[CompanySize]
    headquarters_address: Optional[str]
    hiring_agency: Optional[bool]
    eeo_text: Optional[str]
    website_uri: Optional[str]
    career_site_uri: Optional[str]
    image_uri: Optional[str]
    keyword_searchable_job_custom_attributes: Optional[List[str]]

    # output
    derived_info: Optional[DerivedInfo]
    suspended: Optional[bool]

from enum import Enum, auto
from typing import List, Optional

from pydantic import BaseModel


class LatLng(BaseModel):
    """https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/Location#LatLng"""
    "latitude": number,
    "longitude": number


class PostalAddress(BaseModel):
    """https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/PostalAddress"""
    "revision": number,
    "regionCode": string,
    "languageCode": string,
    "postalCode": string,
    "sortingCode": string,
    "administrativeArea": string,
    "locality": string,
    "sublocality": string,
    "addressLines": [
        string
    ],
    "recipients": [
        string
    ],
    "organization": string


class AutoName(Enum):
    """https://docs.python.org/3/library/enum.html#using-automatic-values"""
    def _generate_next_value_(name, start, count, last_values):
        return name

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
    """https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/Location"""
    "locationType": LocationType
    "postalAddress": PostalAddress
    "latLng": LatLng
    "radiusMiles": number


class DerivedInfo(BaseModel):
    """https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.companies#derivedinfo"""
    headquartersLocation: Location


class CompanySize(AutoName):
    """https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.companies#companysize"""
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

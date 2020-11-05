from typing import List, Optional, Union

from google.cloud import talent
from google.cloud.talent_v4 import CompanySize, Location as CTS_Location
from proto.marshal.collections import Repeated
from pydantic import BaseModel, PrivateAttr, validator

from pytalentsolution import Tenant
from pytalentsolution.cts import CTSModel

client_company = talent.CompanyServiceClient()


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


# class LocationType(AutoName):
#     LOCATION_TYPE_UNSPECIFIED = auto()
#     COUNTRY = auto()
#     ADMINISTRATIVE_AREA = auto()
#     SUB_ADMINISTRATIVE_AREA = auto()
#     LOCALITY = auto()
#     POSTAL_CODE = auto()
#     SUB_LOCALITY = auto()
#     SUB_LOCALITY_1 = auto()
#     SUB_LOCALITY_2 = auto()
#     NEIGHBORHOOD = auto()
#     STREET_ADDRESS = auto()


class Location(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/Location
    """
    location_type: Optional[CTS_Location.LocationType]
    postal_address: Optional[PostalAddress]
    latLng: Optional[LatLng]
    radius_miles: Optional[int]


class DerivedInfo(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.companies#derivedinfo
    """
    headquarters_location: Optional[Location]


# class CompanySize(AutoName):
#     """
#     https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.companies#companysize
#     """
#     COMPANY_SIZE_UNSPECIFIED = auto()
#     MINI = auto()
#     SMALL = auto()
#     SMEDIUM = auto()
#     MEDIUM = auto()
#     BIG = auto()
#     BIGGER = auto()
#     GIANT = auto()

class CompanyInCreate(CTSModel):
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

    @validator("keyword_searchable_job_custom_attributes", pre=True)
    def convert_to_python_list(cls, value):
        if isinstance(value, Repeated):
            value = list(value)
        return value


class CompanyInUpdate(CompanyInCreate):
    name: Optional[str]


class CompanyInRetrieve(CompanyInUpdate):
    """ contain output-only field """
    derived_info: Optional[Union[DerivedInfo]]
    suspended: Optional[bool]

    @validator("derived_info", pre=True)
    def convert_to_python_dict(cls, value):
        if not isinstance(value, dict):
            # WTF: metaclass
            value = value._meta.parent.to_dict(value)
        return value


class Company(CompanyInRetrieve):
    _tenant: Optional[Tenant] = PrivateAttr(None)

    def create(self, tenant: Optional[Tenant] = None):
        """
           Create Company
           https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.companies/create
        """
        if tenant:
            self._tenant = tenant

        company = CompanyInCreate(**self.dict())
        response = client_company.create_company(parent=self._tenant.name,
                                                 company=company.dict(exclude_unset=True, exclude_none=True))
        out = CompanyInRetrieve.from_orm(response)
        self.update_from_pydantic(out)

    @classmethod
    def get(cls, name):
        response = client_company.get_company(name=name)
        return cls.from_orm(response)

    def update(self):
        company = CompanyInUpdate(**self.dict())
        _ = client_company.update_company(company=company.dict(exclude_unset=True, exclude_none=True))

    def delete(self):
        client_company.delete_company(name=self.name)
        self.name = None

    @classmethod
    def list(cls, tenant: Tenant):
        companies = []
        for response in client_company.list_companies(parent=tenant.name):
            company = cls.from_orm(response)
            company._tenant = tenant
            companies.append(company)
        return companies

# TODO: add __all__

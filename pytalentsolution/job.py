from datetime import datetime
from typing import Dict, List, Literal, Optional, TYPE_CHECKING, Union

from google.cloud import talent
from google.cloud.talent import (CompensationInfo as CTS_CompensationInfo, DegreeType, EmploymentType, HtmlSanitization,
                                 JobBenefit, JobCategory, JobLevel, JobView, PostingRegion, Visibility, SearchJobsRequest as CTS_SearchJobsRequest)
from pydantic import BaseModel, Field

# from google.cloud.talent_v4 import CustomAttribute as CTS_CustomAttributes
# from google.cloud.talent_v4.types.common import CustomAttribute as CTS_CustomAttributes
# from google.cloud.talent_v4beta1.types import CustomAttribute as CTS_CustomAttributes
from pytalentsolution import CTSModel, Location, PrivateAttr, Tenant

if TYPE_CHECKING:
    from pytalentsolution.job_search import JobQuery, RequestMetadata

class ApplicationInfo(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.ApplicationInfo
    """
    emails: Optional[List[str]]
    instruction: Optional[str]
    uris: Optional[List[str]]


class Money(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.Money
    """
    currency_code: Optional[str]
    units: Optional[
        int]  # TODO: wtf wtf Docs said it's str type as int64 format, but when I sent it, it error wtf wtf wtf wtf
    nanos: Optional[int]


class CompensationRange(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.CompensationRange
    """
    max_compensation: Optional[Money]
    min_compensation: Optional[Money]


class CompensationEntry(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.CompensationEntry
    """
    type_: Optional[CTS_CompensationInfo.CompensationType]
    unit: Optional[CTS_CompensationInfo.CompensationUnit]
    description: Optional[str]
    expected_units_per_year: Optional[int]

    # Union field compensation_amount can be only one of the following:
    amount: Optional[Money]
    range_: Optional[CompensationRange]
    # End of list of possible types for union field compensation_amount.


class CompensationInfo(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.CompensationInfo
    """
    entries: Optional[List[CompensationEntry]]
    annualized_base_compensation_range: Optional[CompensationRange]
    annualized_total_compensation_range: Optional[CompensationRange]


# class DegreeType(AutoName):
#     """
#     https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/DegreeType
#     """
#     DEGREE_TYPE_UNSPECIFIED = auto()
#     PRIMARY_EDUCATION = auto()
#     LOWER_SECONDARY_EDUCATION = auto()
#     UPPER_SECONDARY_EDUCATION = auto()
#     ADULT_REMEDIAL_EDUCATION = auto()
#     ASSOCIATES_OR_EQUIVALENT = auto()
#     BACHELORS_OR_EQUIVALENT = auto()
#     MASTERS_OR_EQUIVALENT = auto()
#     DOCTORAL_OR_EQUIVALENT = auto()


# class EmploymentType(AutoName):
#     """
#     https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.EmploymentType
#     """
#     EMPLOYMENT_TYPE_UNSPECIFIED = auto()
#     FULL_TIME = auto()
#     PART_TIME = auto()
#     CONTRACTOR = auto()
#     CONTRACT_TO_HIRE = auto()
#     TEMPORARY = auto()
#     INTERN = auto()
#     VOLUNTEER = auto()
#     PER_DIEM = auto()
#     FLY_IN_FLY_OUT = auto()
#     OTHER_EMPLOYMENT_TYPE = auto()


# class JobLevel(AutoName):
#     """
#     https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.JobLevel
#     """
#     JOB_LEVEL_UNSPECIFIED = auto()
#     ENTRY_LEVEL = auto()
#     EXPERIENCED = auto()
#     MANAGER = auto()
#     DIRECTOR = auto()
#     EXECUTIVE = auto()


# class PostingRegion(AutoName):
#     """
#     https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.PostingRegion
#     """
#     POSTING_REGION_UNSPECIFIED = auto()
#     ADMINISTRATIVE_AREA = auto()
#     NATION = auto()
#     TELECOMMUTE = auto()


# class Visibility(AutoName):
#     """
#     https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.Visibility
#     """
#     VISIBILITY_UNSPECIFIED = auto()
#     ACCOUNT_ONLY = auto()
#     SHARED_WITH_GOOGLE = auto()
#     SHARED_WITH_PUBLIC = auto()


# class JobCategory(AutoName):
#     """
#     https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.JobCategory
#     """
#     JOB_CATEGORY_UNSPECIFIED = auto()
#     ACCOUNTING_AND_FINANCE = auto()
#     ADMINISTRATIVE_AND_OFFICE = auto()
#     ADVERTISING_AND_MARKETING = auto()
#     ANIMAL_CARE = auto()
#     ART_FASHION_AND_DESIGN = auto()
#     BUSINESS_OPERATIONS = auto()
#     CLEANING_AND_FACILITIES = auto()
#     COMPUTER_AND_IT = auto()
#     CONSTRUCTION = auto()
#     CUSTOMER_SERVICE = auto()
#     EDUCATION = auto()
#     ENTERTAINMENT_AND_TRAVEL = auto()
#     FARMING_AND_OUTDOORS = auto()
#     HEALTHCARE = auto()
#     HUMAN_RESOURCES = auto()
#     INSTALLATION_MAINTENANCE_AND_REPAIR = auto()
#     LEGAL = auto()
#     MANAGEMENT = auto()
#     MANUFACTURING_AND_WAREHOUSE = auto()
#     MEDIA_COMMUNICATIONS_AND_WRITING = auto()
#     OIL_GAS_AND_MINING = auto()
#     PERSONAL_CARE_AND_SERVICES = auto()
#     PROTECTIVE_SERVICES = auto()
#     REAL_ESTATE = auto()
#     RESTAURANT_AND_HOSPITALITY = auto()
#     SALES_AND_RETAIL = auto()
#     SCIENCE_AND_ENGINEERING = auto()
#     SOCIAL_SERVICES_AND_NON_PROFIT = auto()
#     SPORTS_FITNESS_AND_RECREATION = auto()
#     TRANSPORTATION_AND_LOGISTICS = auto()


class DerivedInfo(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.DerivedInfo
    """
    locations: Optional[List[Location]]
    job_categories: Optional[List[JobCategory]]


# class HtmlSanitization(AutoName):
#     """
#     https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.HtmlSanitization
#     """
#     HTML_SANITIZATION_UNSPECIFIED = auto()
#     HTML_SANITIZATION_DISABLED = auto()
#     SIMPLE_FORMATTING_ONLY = auto()


class ProcessingOptions(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.ProcessingOptions
    """
    disable_street_address_resolution: Optional[bool]
    html_sanitization: Optional[HtmlSanitization]


class CustomAttributes(BaseModel):
    string_values: Optional[List[str]] = None
    long_values: Optional[List[int]] = None
    filterable: Optional[bool] = None
    keyword_searchable: Optional[bool] = None

    def to_protoMessage(self):
        obj = talent.CustomAttribute()
        for k, v in self.dict(exclude_none=True).items():
            setattr(obj, k, v)
        return obj


class JobInCreate(CTSModel):
    company: str
    requisition_id: str
    title: str
    description: str
    addresses: Optional[List[str]]
    application_info: Optional[ApplicationInfo]
    job_benefits: Optional[JobBenefit]
    compensation_info: Optional[CompensationInfo]
    custom_attributes: Optional[Dict[str, Union[CustomAttributes, talent.CustomAttribute]]]
    degree_types: Optional[List[DegreeType]]
    department: Optional[str]
    employment_types: Optional[List[EmploymentType]]
    incentives: Optional[str]
    language_code: Optional[str]
    job_level: Optional[JobLevel]
    promotion_value: Optional[int]
    qualifications: Optional[str]
    responsibilities: Optional[str]
    posting_region: Optional[PostingRegion]
    job_start_time: Optional[datetime]
    job_end_time: Optional[datetime]
    posting_publish_time: Optional[datetime]
    posting_expire_time: Optional[datetime]

    # deprecated
    visibility: Optional[Visibility]

    def prepare_for_rpc(self):
        if self.custom_attributes:
            for k, v in self.custom_attributes.items():
                if isinstance(v, CustomAttributes):
                    self.custom_attributes[k] = v.to_protoMessage()
        return self


class JobInUpdate(JobInCreate):
    name: Optional[str]


class JobInRetrieve(JobInUpdate):
    # output
    posting_create_time: Optional[str]
    posting_update_time: Optional[str]
    company_display_name: Optional[str]
    derived_info: Optional[DerivedInfo]
    processing_options: Optional[ProcessingOptions]


client_job = talent.JobServiceClient()


class Job(JobInRetrieve):
    _tenant: Optional[Tenant] = PrivateAttr(None)

    def create(self, tenant: Optional[Tenant] = None):
        """
           Create Job
           https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.companys.jobs/create
        """
        if tenant:
            self._tenant = tenant
        
        job = JobInCreate(**self.dict())
        # job = job.dict(exclude_unset=True, exclude_none=True)
        job = job.prepare_for_rpc().dict(exclude_unset=True, exclude_none=True)
        job = talent.Job(**job)
        response = client_job.create_job(
                parent=self._tenant.name,
                job=job
        )
        out = JobInRetrieve(**self.proto_to_dict(response))
        self.update_from_pydantic(out)

    @classmethod
    def get(cls, name):
        """
        Create Job
        https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/create
        """
        response = client_job.get_job(name=name)
        return cls(**cls.proto_to_dict(response))

    def update(self):
        """
        Update Job
        https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/patch
        """
        job = JobInUpdate(**self.dict())
        job = job.prepare_for_rpc().dict(exclude_unset=True, exclude_none=True)
        job = talent.Job(**job)
        _ = client_job.update_job(
                job=job
        )

    def delete(self):
        """
        Delete Job
        https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/delete
        """
        client_job.delete_job(name=self.name)
        self.name = None

    class Filter(BaseModel):
        companyName: str = Field(..., alias='company_name')
        requisitionId: Optional[str] = Field(None, alias='requisition_id')
        status: Optional[Literal['OPEN', 'EXPIRED', 'ALL']]

        def __str__(self):
            from pypika import Field, Criterion

            filter_ = []
            for var_name in self.__fields__:
                value = getattr(self, var_name)
                if value:
                    field = Field(var_name)
                    filter_.append(field == value)
            return str(Criterion.all(filter_))

    @classmethod
    def list(cls, tenant: Tenant, **kwargs):
        """
        List Job
        https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/list
        """
        list_filter = cls.Filter(**kwargs)

        jobs = []
        for response in client_job.list_jobs(parent=tenant.name, filter=str(list_filter)):
            job = cls.from_orm(response)
            job._tenant = tenant
            jobs.append(job)
        return jobs

    @classmethod
    def search_jobs(
                    cls, 
                    tenant: Tenant, 
                    job_query: "JobQuery", 
                    request_metadata: "RequestMetadata",
                    job_view : JobView = JobView.JOB_VIEW_ID_ONLY,
                    search_mode : CTS_SearchJobsRequest.SearchMode = CTS_SearchJobsRequest.SearchMode.JOB_SEARCH,
                    max_page_size : int = 9,
                    offset : int = 0,
                    next_page_token : str = None
                    ):
        """
        https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/search

        Returns:
            response (SearchJobResponse) : iterator
        """

        if offset and next_page_token:
            request = talent.SearchJobsRequest(parent=tenant.name,
                                            request_metadata=request_metadata.dict(exclude_unset=True),
                                            job_query=job_query.dict(exclude_unset=True),
                                            job_view=job_view,
                                            search_mode=search_mode,
                                            max_page_size=max_page_size,
                                            page_token=next_page_token,
                                            offset=offset)
            response = client_job.search_jobs(request=request)            

            return cls.proto_to_dict(response)

        if offset:
            request = talent.SearchJobsRequest(parent=tenant.name,
                                            request_metadata=request_metadata.dict(exclude_unset=True),
                                            job_query=job_query.dict(exclude_unset=True),
                                            job_view=job_view,
                                            search_mode=search_mode,
                                            max_page_size=max_page_size,
                                            offset=offset)
            response = client_job.search_jobs(request=request)            

            return cls.proto_to_dict(response)

        if next_page_token:
            request = talent.SearchJobsRequest(parent=tenant.name,
                                            request_metadata=request_metadata.dict(exclude_unset=True),
                                            job_query=job_query.dict(exclude_unset=True),
                                            job_view=job_view,
                                            search_mode=search_mode,
                                            max_page_size=max_page_size,
                                            page_token=next_page_token)
            response = client_job.search_jobs(request=request)

            return cls.proto_to_dict(response) 

        request = talent.SearchJobsRequest(parent=tenant.name,
                                        request_metadata=request_metadata.dict(exclude_unset=True),
                                        job_query=job_query.dict(exclude_unset=True),
                                        job_view=job_view,
                                        search_mode=search_mode,
                                        max_page_size=max_page_size)
        response = client_job.search_jobs(request=request)

        return cls.proto_to_dict(response)            

# def search_job_auto_complete():
#     """
#     https://cloud.google.com/talent-solution/job-search/docs/autocomplete
#     """
#     pass

# def batch_create_job(tenant : Tenant, job : List[Job]):
#     """
#     Batch Create Job
#     https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/batchCreate
#     Args:
#         tenant (Tenant): Tenant object
#         job (Job): Job object
#     Returns:
#         response.name: The job path `projects/project_id/tenant/tenant_id/company/company_id/job/job_id`
#     """
#     try:
#         response = client_job.batch_create_jobs(parent = tenant.name, job = job)
#         return response.name
#     except Exception as e:
#         raise e

# def batch_update_job(job : List[Job]):
#     """
#     Batch Update Job
#     https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/batchUpdate
#     Args:
#         job (List[Job]): List Job object
#     Returns:
#         response.name: The job path `projects/project_id/tenant/tenant_id/company/company_id/job/job_id`
#     """
#     try:
#         response = client_job.batch_update_job(job = job)
#         return response.name
#     except Exception as e:
#         raise e

# def batch_delete_job(job : List[Job]):
#     """
#     Batch Delete Job
#     https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/batchDelete
#     Args:
#         job (Job): Job object
#     """
#     try:
#         response = client_job.batch_delete_job(names = job)
#     except Exception as e:
#         raise e

# TODO: add __all__

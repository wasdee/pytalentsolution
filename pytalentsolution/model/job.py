from enum import auto
from typing import List, Optional, Dict

from pydantic import BaseModel

from pytalentsolution.model.company import AutoName, Location


class ApplicationInfo(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.ApplicationInfo
    """
    emails: Optional[List[str]]
    instruction: Optional[str]
    uris: Optional[List[str]]


class JobBenefit(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.JobBenefit
    """
    JOB_BENEFIT_UNSPECIFIED = auto()
    CHILD_CARE = auto()
    DENTAL = auto()
    DOMESTIC_PARTNER = auto()
    FLEXIBLE_HOURS = auto()
    MEDICAL = auto()
    LIFE_INSURANCE = auto()
    PARENTAL_LEAVE = auto()
    RETIREMENT_PLAN = auto()
    SICK_DAYS = auto()
    VACATION = auto()
    VISION = auto()


class CompensationType(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.CompensationInfo
    """
    COMPENSATION_TYPE_UNSPECIFIED = auto()
    BASE = auto()
    BONUS = auto()
    SIGNING_BONUS = auto()
    EQUITY = auto()
    PROFIT_SHARING = auto()
    COMMISSIONS = auto()
    TIPS = auto()
    OTHER_COMPENSATION_TYPE = auto()


class CompensationUnit(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.CompensationUnit
    """
    COMPENSATION_UNIT_UNSPECIFIED = auto()
    HOURLY = auto()
    DAILY = auto()
    WEEKLY = auto()
    MONTHLY = auto()
    YEARLY = auto()
    ONE_TIME = auto()
    OTHER_COMPENSATION_UNIT = auto()


class Money(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.Money
    """
    currencyCode: Optional[str]
    units: Optional[str]
    nanos: Optional[int]


class CompensationRange(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.CompensationRange
    """
    maxCompensation: Optional[Money]
    minCompensation: Optional[Money]


class CompensationEntry(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.CompensationEntry
    """
    type: Optional[CompensationType]
    unit: Optional[CompensationUnit]
    description: Optional[str]
    expectedUnitsPerYear: Optional[int]

    # Union field compensation_amount can be only one of the following:
    amount: Optional[Money]
    range: Optional[CompensationRange]
    # End of list of possible types for union field compensation_amount.


class CompensationInfo(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.CompensationInfo
    """
    entries: Optional[List[CompensationEntry]]
    annualized_base_compensation_range: Optional[CompensationRange]
    annualizedTotal_compensation_range: Optional[CompensationRange]


class DegreeType(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/DegreeType
    """
    DEGREE_TYPE_UNSPECIFIED = auto()
    PRIMARY_EDUCATION = auto()
    LOWER_SECONDARY_EDUCATION = auto()
    UPPER_SECONDARY_EDUCATION = auto()
    ADULT_REMEDIAL_EDUCATION = auto()
    ASSOCIATES_OR_EQUIVALENT = auto()
    BACHELORS_OR_EQUIVALENT = auto()
    MASTERS_OR_EQUIVALENT = auto()
    DOCTORAL_OR_EQUIVALENT = auto()


class EmploymentType(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.EmploymentType
    """
    EMPLOYMENT_TYPE_UNSPECIFIED = auto()
    FULL_TIME = auto()
    PART_TIME = auto()
    CONTRACTOR = auto()
    CONTRACT_TO_HIRE = auto()
    TEMPORARY = auto()
    INTERN = auto()
    VOLUNTEER = auto()
    PER_DIEM = auto()
    FLY_IN_FLY_OUT = auto()
    OTHER_EMPLOYMENT_TYPE = auto()


class JobLevel(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.JobLevel
    """
    JOB_LEVEL_UNSPECIFIED = auto()
    ENTRY_LEVEL = auto()
    EXPERIENCED = auto()
    MANAGER = auto()
    DIRECTOR = auto()
    EXECUTIVE = auto()


class PostingRegion(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.PostingRegion
    """
    POSTING_REGION_UNSPECIFIED = auto()
    ADMINISTRATIVE_AREA = auto()
    NATION = auto()
    TELECOMMUTE = auto()


class Visibility(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.Visibility
    """
    VISIBILITY_UNSPECIFIED = auto()
    ACCOUNT_ONLY = auto()
    SHARED_WITH_GOOGLE = auto()
    SHARED_WITH_PUBLIC = auto()


class JobCategory(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.JobCategory
    """
    JOB_CATEGORY_UNSPECIFIED = auto()
    ACCOUNTING_AND_FINANCE = auto()
    ADMINISTRATIVE_AND_OFFICE = auto()
    ADVERTISING_AND_MARKETING = auto()
    ANIMAL_CARE = auto()
    ART_FASHION_AND_DESIGN = auto()
    BUSINESS_OPERATIONS = auto()
    CLEANING_AND_FACILITIES = auto()
    COMPUTER_AND_IT = auto()
    CONSTRUCTION = auto()
    CUSTOMER_SERVICE = auto()
    EDUCATION = auto()
    ENTERTAINMENT_AND_TRAVEL = auto()
    FARMING_AND_OUTDOORS = auto()
    HEALTHCARE = auto()
    HUMAN_RESOURCES = auto()
    INSTALLATION_MAINTENANCE_AND_REPAIR = auto()
    LEGAL = auto()
    MANAGEMENT = auto()
    MANUFACTURING_AND_WAREHOUSE = auto()
    MEDIA_COMMUNICATIONS_AND_WRITING = auto()
    OIL_GAS_AND_MINING = auto()
    PERSONAL_CARE_AND_SERVICES = auto()
    PROTECTIVE_SERVICES = auto()
    REAL_ESTATE = auto()
    RESTAURANT_AND_HOSPITALITY = auto()
    SALES_AND_RETAIL = auto()
    SCIENCE_AND_ENGINEERING = auto()
    SOCIAL_SERVICES_AND_NON_PROFIT = auto()
    SPORTS_FITNESS_AND_RECREATION = auto()
    TRANSPORTATION_AND_LOGISTICS = auto()


class DerivedInfo(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.DerivedInfo
    """
    locations: Optional[List[Location]]
    job_categories: Optional[List[JobCategory]]


class HtmlSanitization(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.HtmlSanitization
    """
    HTML_SANITIZATION_UNSPECIFIED = auto()
    HTML_SANITIZATION_DISABLED = auto()
    SIMPLE_FORMATTING_ONLY = auto()


class ProcessingOptions(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job.ProcessingOptions
    """
    disable_street_address_resolution: Optional[bool]
    html_sanitization: Optional[HtmlSanitization]

class Job(BaseModel):
    name: Optional[str]
    company: str
    requisition_id: str
    title: str
    description: str
    addresses: Optional[List[str]]
    application_info: Optional[ApplicationInfo]
    job_benefits: Optional[JobBenefit]
    compensation_info: Optional[CompensationInfo]
    custom_attributes: Optional[Dict[str, Dict]]
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
    job_start_time: Optional[str]
    job_end_time: Optional[str]
    posting_publish_time: Optional[str]
    posting_expire_time: Optional[str]

    # deprecated
    visibility: Optional[Visibility]

    # output
    posting_create_time: Optional[str]
    posting_update_time: Optional[str]
    company_display_name: Optional[str]
    derived_info: Optional[DerivedInfo]
    processing_options: Optional[ProcessingOptions]

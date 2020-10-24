from enum import auto
from typing import List, Optional, Dict

from pydantic import BaseModel

from pytalentsolution.model.company import LatLng
from pytalentsolution.model.job import Money, JobCategory, EmploymentType, CompensationRange
from pytalentsolution.model.enum_util import AutoName

class SearchMode(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/SearchMode
    """
    JOB_BENEFIT_UNSPECIFIED = auto()
    JOB_SEARCH = auto()
    FEATURED_JOB_SEARCH = auto()

class DeviceType(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/RequestMetadata#DeviceType
    """
    DEVICE_TYPE_UNSPECIFIED = auto()
    WEB = auto()
    MOBILE_WEB = auto()
    ANDROID = auto()
    IOS = auto()
    BOT = auto()
    OTHER = auto()

class DeviceInfo(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/RequestMetadata#DeviceInfo
    """
    device_type : Optional[DeviceType]
    id : Optional[str]

class RequestMetadata(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/RequestMetadata
    """
    domain : str
    session_id : str
    user_id : str
    allow_missing_ids : Optional[bool]
    device_info : Optional[DeviceInfo]

class CommuteMethod(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery#CommuteMethod
    """
    COMMUTE_METHOD_UNSPECIFIED = auto()
    DRIVING = auto()
    TRANSIT = auto()

class RoadTraffic(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery#RoadTraffic
    """
    ROAD_TRAFFIC_UNSPECIFIED = auto()
    TRAFFIC_FREE = auto()
    BUSY_HOUR = auto()

class TimeOfDay(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery#TimeOfDay
    """
    hours : Optional[int]
    minutes : Optional[int]
    seconds : Optional[int]
    nanos : Optional[int]

class CommuteFilter(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery#CommuteFilter
    """
    commute_method : CommuteMethod
    start_coordinates : LatLng
    travel_duration : str
    allow_imprecise_addresses : Optional[bool]
    road_traffic : Optional[RoadTraffic]
    departure_time : Optional[TimeOfDay] 

class FilterType(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery#FilterType
    """
    FILTER_TYPE_UNSPECIFIED  = auto()
    UNIT_ONLY = auto()
    UNIT_AND_AMOUNT = auto()
    ANNUALIZED_BASE_AMOUNT = auto()
    ANNUALIZED_TOTAL_AMOUNT = auto()

class CompesationUnit(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#CompensationUnit
    """
    COMPENSATION_UNIT_UNSPECIFIED = auto()
    HOURLY = auto()
    DAILY = auto()
    WEEKLY = auto()
    MONTHLY = auto()
    YEARLY = auto()
    ONE_TIME = auto()
    OTHER_COMPENSATION_UNIT = auto()

class CompensationFilter(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery#CompensationFilter
    """
    type : FilterType
    units : List[CompesationUnit]
    range : Optional[CompensationRange]
    include_jobs_with_unspecified_compensation_range : Optional[bool]

class TimestampRange(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery#TimestampRange
    """
    start_time : Optional[str]
    end_time : Optional[str]

class JobQuery(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery
    """
    query : str
    query_language_code : Optional[str]
    companies : Optional[List[str]]
    job_categories : Optional[List[JobCategory]]
    commute_filter : Optional[CommuteFilter]
    company_display_name : Optional[List]
    compensation_filter : Optional[CompensationFilter]
    custom_attribute_filter : Optional[str]
    disable_spell_check : Optional[bool]
    employment_types : Optional[List[EmploymentType]]
    language_codes : Optional[List[str]]
    publish_time_range : Optional[TimestampRange]
    excluded_jobs : Optional[List[str]]

class TelecommutePreference(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery#TelecommutePreference
    """
    TELECOMMUTE_PREFERENCE_UNSPECIFIED = auto()
    TELECOMMUTE_EXCLUDED = auto()
    TELECOMMUTE_ALLOWED = auto()

class LocationFilter(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery#LocationFilter
    """
    address : Optional[str]
    region_code : Optional[str]
    lat_lng : Optional[LatLng]
    distance_in_miles : Optional[int]
    telecommute_preference : Optional[TelecommutePreference]

class HistogramQuery(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/HistogramQuery
    """
    histogram_query : Optional[str]

class JobView(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobView
    """
    JOB_VIEW_UNSPECIFIED = auto()
    JOB_VIEW_ID_ONLY = auto()
    JOB_VIEW_MINIMAL = auto()
    JOB_VIEW_SMALL = auto()
    JOB_VIEW_FULL = auto()

class DiversificationLevel(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/DiversificationLevel
    """
    DIVERSIFICATION_LEVEL_UNSPECIFIED = auto()
    DISABLED = auto()
    SIMPLE = auto()

class ImportanceLevel(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/CustomRankingInfo#ImportanceLevel
    """
    IMPORTANCE_LEVEL_UNSPECIFIED = auto()
    NONE = auto()
    LOW = auto()
    MILD = auto()
    MEDIUM = auto()
    HIGH = auto()
    EXTREME = auto()

class CustomRankingInfo(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/CustomRankingInfo
    """
    importance_level : ImportanceLevel
    ranking_expression : str

class SearchJobsRequest(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/search
    """
    search_mode : Optional[SearchMode]
    request_metada : RequestMetadata
    job_query : Optional[JobQuery]
    enable_broadening : Optional[bool]
    histogram_queries : Optional[List[HistogramQuery]]
    job_view : Optional[JobView]
    offset : Optional[int]
    max_page_size : Optional[int]
    page_token : Optional[str]
    order_by : Optional[str]
    diversification_level : Optional[DiversificationLevel]
    custom_ranking_info : Optional[CustomRankingInfo]
    disable_keyword_match : Optional[bool]
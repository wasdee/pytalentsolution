from enum import auto
from typing import Optional, List

from autoname import AutoName
from google.cloud import talent
from pydantic import BaseModel

from pytalentsolution import Tenant


class JobEventType(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/ClientEvent#JobEventType
    """
    JOB_EVENT_TYPE_UNSPECIFIED = auto()
    IMPRESSION = auto()
    VIEW = auto()
    VIEW_REDIRECT = auto()
    APPLICATION_START = auto()
    APPLICATION_FINISH = auto()
    APPLICATION_QUICK_SUBMISSION = auto()
    APPLICATION_REDIRECT = auto()
    APPLICATION_START_FROM_SEARCH = auto()
    APPLICATION_REDIRECT_FROM_SEARCH = auto()
    APPLICATION_COMPANY_SUBMIT = auto()
    BOOKMARK = auto()
    NOTIFICATION = auto()
    HIRED = auto()
    SENT_CV = auto()
    INTERVIEW_GRANTED = auto()


class JobEvent(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/ClientEvent#JobEvent
    """
    type: JobEventType
    jobs: List[str]
    profile: Optional[str]


class ProfileEventType(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/ClientEvent#ProfileEventType
    """
    PROFILE_EVENT_TYPE_UNSPECIFIED = auto()
    IMPRESSION = auto()
    VIEW = auto()
    BOOKMARK = auto()


class ProfileEvent(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/ClientEvent#ProfileEvent
    """
    type: ProfileEventType
    profiles: List[str]
    jobs: Optional[List[str]]


client_event = talent.EventServiceClient()


class ClientEvent(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/ClientEvent
    """
    request_id: Optional[str]
    event_id: str
    create_time: str  # google RPC require timestamp obj ???
    event_notes: Optional[str]

    # Union field 'event' can be only one of the following:
    job_event: Optional[JobEvent]
    profile_event: Optional[ProfileEvent]

    # End of list of possible types for union field 'event'.

    def create(self, tenant: Tenant):
        # TODO: test
        response = client_event.create_client_event(parent=tenant.name, client_event=self.dict(exclude_unset=True))
        return response

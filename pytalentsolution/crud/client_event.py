from pytalentsolution.model.tenant import Tenant 
from pytalentsolution.model.company import Company 
from pytalentsolution.model.job import Job
from pytalentsolution.model.client_event import ClientEvent
from pytalentsolution.model.job_search import SearchJobsRequest, JobQuery, RequestMetadata
from pytalentsolution import project_id

from google.cloud import talent

client_event = talent.EventServiceClient()

def create_client_event(tenant : Tenant, event : ClientEvent):
    """
    Create Client Event
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.clientEvents/create
    Args:
        tenant (Tenant): Tenant object
        event (ClientEvent): ClientEvent object
    Returns:
        response: JSON
    """
    try:
        response = client_event.create_client_event(parent=tenant.name, client_event=event.dict(exclude_unset=True))
        return response
    except Exception as e:
        raise e
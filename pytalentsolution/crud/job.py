from pytalentsolution.model.tenant import Tenant
from pytalentsolution.job import Job
from pytalentsolution.model.job_search import JobQuery, RequestMetadata

from google.cloud import talent


client_job = talent.JobServiceClient()



def search_jobs(tenant : Tenant, job_query : JobQuery, request_metadata : RequestMetadata):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/search
    Args: 
        tenant (Tenant) : Tenant object
        job_query (JobQuery) : JobQuery object
        request_metada (RequestMedata) : RequestMedata object
    Returns:
        response (SearchJobResponse) : iterator
    """
    try:
        request = talent.SearchJobsRequest(parent=tenant.name,
                                            request_metadata=request_metadata.dict(exclude_unset=True),
                                            job_query=job_query.dict(exclude_unset=True))
        response = client_job.search_jobs(request=request)
        return response
    except Exception as e:
        raise e


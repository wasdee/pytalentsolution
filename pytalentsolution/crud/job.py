from pytalentsolution.model.tenant import Tenant 
from pytalentsolution.model.company import Company 
from pytalentsolution.model.job import Job
from pytalentsolution.model.job_search import SearchJobsRequest, JobQuery, RequestMetadata
from pytalentsolution import project_id

from google.cloud import talent


client_job = talent.JobServiceClient()

def create_job(tenant : Tenant, job : Job) -> str:
    """
    Create Job
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/create
    Args:
        tenant (Tenant): Tenant object
        job (Job): Job object
    Returns:
        response.name: The job path `projects/project_id/tenant/tenant_id/company/company_id/job/job_id`
    """
    try: 
        response = client_job.create_job(parent = tenant.name, job = job.dict(exclude_unset=True))
        return response.name
    except Exception as e:
        raise e

def get_job(job : Job) -> Job:
    """
    Get Job
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/get
    Args:
        job (Job): Job object
    Returns:
        response: The job object`
    """
    try: 
        response = client_job.get_job(name = job.name)
        return response
    except Exception as e:
        raise e

def update_job(job : Job) -> str:
    """
    Update Job
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/patch
    Args:
        job (Job): Job object
    Returns:
        response.name: The job path `projects/project_id/tenant/tenant_id/company/company_id/job/job_id`
    """
    try: 
        response = client_job.update_job(job = job.dict(exclude_unset=True))
        return response.name
    except Exception as e:
        raise e

def delete_job(job : Job):
    """
    Delete Job
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/delete
    Args:
        job (Job): Job object
    """
    try: 
        response = client_job.delete_job(name = job.name)
    except Exception as e:
        raise e

def list_job(tenant : Tenant, filter_ : str) -> list:
    """
    List Job
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/list
    Args:
        tenant (Tenant): Tenant object
        filter_ (str): 'companyName="projects/my-project/companies/company-id"'

    Returns:
        results (list): The job object`
    """
    try: 
        results = []
        for job in client_job.list_jobs(parent=tenant.name,filter=filter_):
            results.append(job)
        return results
    except Exception as e:
        raise e

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
from pytalentsolution.model.tenant import Tenant 
from pytalentsolution import project_id

from google.cloud import talent

client_tenant = talent.TenantServiceClient()

def create_tenant(tenant : Tenant) -> str:
    """
    Create Tenant for scoping resources, e.g. companies and jobs
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants/create

    Args:
         tenant (Tenant): Tenant object
    Returns:
        response.name: The talent path `projects/project_id/tenant/tenant_id`
    """
    try:
        parent = f"projects/{project_id}"
        tenant = talent.Tenant(external_id = tenant.external_id, name = tenant.name)
        response = client_tenant.create_tenant(parent = parent, tenant = tenant)
        return response.name
    except Exception as e:
        raise e

def get_tenant(tenant : Tenant) -> Tenant:
    """
    Get Tenant by name
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants/get

    Args:
        tenant (Tenant): Tenant object
    Returns:
        response (tenant object) : The response of talent object included `name`, `externalId` field.
    """
    try:
        response = client_tenant.get_tenant(name = tenant.name)
        return response
    except Exception as e:
        raise e

def update_tenant(tenant : Tenant) -> Tenant:
    """
    update the external_id 
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants/patch
    
    Args:
        tenant (Tenant): Tenant object
    Returns:
        response: talent response object with [name, external_id]
    """    
    try:
        tenant = talent.Tenant(name=tenant.name, external_id=tenant.external_id)
        response = client_tenant.update_tenant(tenant=tenant)
        return response
    except Exception as e:
        raise e

def delete_tenant(tenant : Tenant):
    """
    Delete Tenant by name
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants/delete

    Args:
        tenant (Tenant): Tenant object
    """
    try:
        client_tenant.delete_tenant(name = tenant.name)
    except Exception as e:
        raise e

def list_tenant() -> list:
    """
    Get Tenants List
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants/list

    Returns:
        response (list (tuple)) : The list of talent included (`name`, `external_id`) field.
    """
    try:
        parent = f"projects/{project_id}"
        tenant_list = []
        for tenant in client_tenant.list_tenants(parent = parent):
            tenant_list.append((tenant.name, tenant.external_id))
        return tenant_list
    except Exception as e:
        raise e
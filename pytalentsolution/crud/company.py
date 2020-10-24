from pytalentsolution.model.tenant import Tenant 
from pytalentsolution.model.company import Company 
from pytalentsolution import project_id

from google.cloud import talent

client_companies = talent.CompanyServiceClient()

def create_company(tenant : Tenant, company : Company) -> str:
    """
    Create Company
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.companies/create

    Args:
        tenant (Tenant): Tenant object
        company (Company) : Company object
    Returns:
        response.name: The companies path `projects/project_id/tenant/tenant_id/companies/companies_id`
    """
    try:
        response = client_companies.create_company(parent = tenant.name, company = company.dict(exclude_unset=True))
        return response.name
    except Exception as e:
        raise e

def get_company(company : Company) -> Company:
    """
    Get Company
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.companies/get

    Args:
        company (Company) : Company object
    Returns:
        response (Company) : The companies object
    """    
    try: 
        response = client_companies.get_company(name = company.name)
        return response
    except Exception as e:
        raise e

def update_company(company : Company) -> Company:
    """
    Update Company
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.companies/patch

    Args:
        company (Company) : Company object
    Returns:
        response (Company) : The companies object
    """    
    try: 
        response = client_companies.update_company(company = company.dict(exclude_unset=True))
        return response
    except Exception as e:
        raise e

def delete_company(company : Company):
    """
    Update Company
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.companies/patch

    Args:
        company (Company) : Company object
    """   
    try: 
        client_companies.delete_company(name = company.name)
    except Exception as e:
        raise e

def list_company(tenant : Tenant) -> list:
    """
    List Company
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.companies/list
    Args:
        tenant (Tenant): Tenant object
        company (Company) : Company object
    Returns:
        companies_list (list) : The list of company object
    """   
    try:
        companies_list = []
        for company in client_companies.list_companies(parent = tenant.name):
            companies_list.append(company)
        return companies_list
    except Exception as e:
        raise e
    
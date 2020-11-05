from pytalentsolution.crud.tenant import create_tenant
from pytalentsolution.company import Company
from pytalentsolution.job import Job
from pytalentsolution.tenant import Tenant


def test_job_with_custom_attr():
    tenant_obj = Tenant(external_id="test_tenant")
    company_obj = Company(display_name="github", external_id="1")
    job_obj = Job(company="", requisition_id="1", title="engineer", description="implement system")

    tenant_obj = create_tenant(tenant=tenant_obj)
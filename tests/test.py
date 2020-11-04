from pytalentsolution.model.tenant import Tenant
from pytalentsolution.model.company import Company, CompanySize
from pytalentsolution.model.client_event import ClientEvent
from pytalentsolution.model.job import Job, EmploymentType, CustomAttributes
from pytalentsolution.model.job_search import JobQuery, RequestMetadata
from pytalentsolution.crud.tenant import create_tenant, get_tenant, delete_tenant, update_tenant
from pytalentsolution.crud.company import create_company, get_company, update_company, delete_company
from pytalentsolution.crud.job import create_job, get_job, update_job, delete_job, search_jobs
from pytalentsolution.crud.client_event import create_client_event

import unittest

tenant_obj = Tenant(external_id = "pytelentsolution")
company_obj = Company(display_name = "github", external_id = "1")
job_obj = Job(company="",requisition_id="1",title="engineer",description="implement system")

class TestFlow(unittest.TestCase):
    def test_step_a(self):
        """ Create Tenant """
        tenant_obj.name = create_tenant(tenant=tenant_obj)
        self.assertIsInstance(tenant_obj.name, str, msg = "Create Tenant")        

    def test_step_b(self):
        """ Get Tenant """
        result = get_tenant(tenant=tenant_obj)
        self.assertIsNotNone(result, msg = "Get Tenant") 

    def test_step_c(self):
        """ Update Tenant """
        tenant_obj.external_id = "pytalentsolution_dev"
        result = update_tenant(tenant=tenant_obj)
        self.assertIsNotNone(result, msg = "Get Tenant") 
        result = get_tenant(tenant=tenant_obj)
        self.assertEqual(result.external_id, "pytalentsolution_dev", msg = "Validate Update")

    def test_step_d(self):
        """ Create Company """
        company_obj.name = create_company(tenant=tenant_obj, company=company_obj)
        self.assertIsInstance(company_obj.name, str, msg = "Create Company") 

    def test_step_e(self):
        """ Get Company """
        result = get_company(company=company_obj)
        self.assertIsNotNone(result, msg = "Get Company")

    def test_step_f(self):
        """ Update Company """
        company_obj.display_name = "github_v2"
        company_obj.size = CompanySize.BIG
        result = update_company(company=company_obj)
        self.assertIsNotNone(result, msg = "Update Company")
        result = get_company(company=company_obj)
        self.assertEqual(result.display_name, "github_v2",msg = "Validate Update")
        self.assertEqual(result.size, CompanySize.BIG ,msg = "Validate Update")

    def test_step_g(self):
        """ Create Job """
        job_obj.company = company_obj.name.split("/")[-1]
        job_obj.name = create_job(tenant=tenant_obj, job=job_obj)
        self.assertIsInstance(job_obj.name, str, msg = "Create Job")

    def test_step_h(self):
        """ Get Job """
        result = get_job(job=job_obj)
        self.assertIsNotNone(result, msg = "Get Job")

    def test_step_i(self):
        """ Update Job """
        # import pdb; pdb.set_trace()
        job_obj.title = "worker"
        job_obj.employment_types = [EmploymentType.FULL_TIME]
        custom_obj = CustomAttributes()
        custom_obj.string_values = ["hello"]
        custom_obj.filterable = True
        custom_obj.keyword_searchable = True
        print(custom_obj)
        job_obj.custom_attributes["ping"] = custom_obj
        print(job_obj)
        result = update_job(job=job_obj)
        self.assertIsNotNone(result, msg = "Update Job")
        result = get_job(job=job_obj)
        self.assertEqual(result.title, "worker",msg = "Validate Update")
        self.assertEqual(result.employment_types, [EmploymentType.FULL_TIME] ,msg = "Validate Update")


    # def test_step_j(self):
    #     """ Create client event """
    #     client_obj = ClientEvent(event_id="1", create_time = "2020-10-24 10:00:00")
    #     client_obj.event_notes = "test"
    #     client_obj.request_id = "1"
    #     result = create_client_event(tenant=tenant_obj, event= client_obj)
    #     print(result)
    #     self.assertIsNotNone(result, msg = "client event")

    def test_step_k(self):
        """ Search Query """
        job_query_obj = JobQuery(query="worker")
        request_metadata_obj = RequestMetadata(domain="pytalentsolution", session_id="1",user_id="tester")
        result = search_jobs(tenant=tenant_obj,job_query=job_query_obj,request_metadata=request_metadata_obj)
        self.assertIsNotNone(result.matching_jobs, msg = "Search Job")

    ## clear instance
    def test_step_l(self):
        """ Delete Job """
        result = delete_job(job=job_obj)
        self.assertIsNone(result, msg = "Delete Job")        

    def test_step_m(self):
        """ Delete Company """
        result = delete_company(company=company_obj)
        self.assertIsNone(result, msg = "Delete Company")

    def test_step_n(self):
        """ Delete Tenant """
        result = delete_tenant(tenant=tenant_obj)
        self.assertIsNone(result, msg = "Delete Tenant")

if __name__ == "__main__":
    unittest.main()
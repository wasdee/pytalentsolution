from pytalentsolution.model.tenant import Tenant
from pytalentsolution.model.company import Company
from pytalentsolution.model.job import Job
from pytalentsolution.crud.tenant import create_tenant, get_tenant, delete_tenant
from pytalentsolution.crud.company import create_company, get_company, update_company, delete_company
from pytalentsolution.crud.job import create_job, get_job, update_job, delete_job

import unittest

tenant_obj = Tenant(external_id = "pytelentsolution")
company_obj = Company(display_name = "github", external_id = "1")
job_obj = Job(company="",requisition_id="1",title="engineer",description="implement system")

class TestFlow(unittest.TestCase):
    def test_step_1(self):
        """ Create Tenant """
        tenant_obj.name = create_tenant(tenant=tenant_obj)
        self.assertIsInstance(tenant_obj.name, str, msg = "Create Tenant")        

    def test_step_2(self):
        """ Get Tenant """
        result = get_tenant(tenant=tenant_obj)
        self.assertIsNotNone(result, msg = "Get Tenant") 

    def test_step_3(self):
        """" Create Company """
        company_obj.name = create_company(tenant=tenant_obj, company=company_obj)
        self.assertIsInstance(company_obj.name, str, msg = "Create Company") 

    def test_step_4(self):
        """ Get Company """
        result = get_company(company=company_obj)
        self.assertIsNotNone(result, msg = "Get Company")

    def test_step_5(self):
        """ Update Company """
        company_obj.display_name = "github_v2"
        result = update_company(company=company_obj)
        self.assertIsNotNone(result, msg = "Update Company")
        result = get_company(company=company_obj)
        self.assertEqual(result.display_name, "github_v2",msg = "Validate Update")

    def test_step_6(self):
        """ Create Job """
        job_obj.company = company_obj.name.split("/")[-1]
        job_obj.name = create_job(tenant=tenant_obj, job=job_obj)
        self.assertIsInstance(job_obj.name, str, msg = "Create Job")

    def test_step_7(self):
        """ Get Job """
        result = get_job(job=job_obj)
        self.assertIsNotNone(result, msg = "Get Job")

    def test_step_8(self):
        """ Update Job """
        job_obj.title = "worker"
        result = update_job(job=job_obj)
        self.assertIsNotNone(result, msg = "Update Job")
        result = get_job(job=job_obj)
        self.assertEqual(result.title, "worker",msg = "Validate Update")

    def test_step_9(self):
        """ Delete Job """
        result = delete_job(job=job_obj)
        self.assertIsNone(result, msg = "Delete Job")        

    def test_step_a(self):
        """ Delete Company """
        result = delete_company(company=company_obj)
        self.assertIsNone(result, msg = "Delete Company")

    def test_step_b(self):
        """ Delete Tenant """
        result = delete_tenant(tenant=tenant_obj)
        self.assertIsNone(result, msg = "Delete Tenant")


if __name__ == "__main__":
    unittest.main()
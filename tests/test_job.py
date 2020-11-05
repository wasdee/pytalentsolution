from uuid import uuid4

from pytalentsolution import CustomAttributes, EmploymentType, Job, JobQuery, RequestMetadata


def test_job_with_custom_attr(tenant, company):
    j = Job(
            company=company.name,
            requisition_id=uuid4().hex,
            title="engineer",
            description="implement system",
            custom_attributes={
                "tags": CustomAttributes(
                        string_values=["hello"],
                        filterable=True,
                        keyword_searchable=True
                )
            }
    )
    j.create(tenant=tenant)

    """ Update Job """
    j.title = "worker"
    j.employment_types = [EmploymentType.FULL_TIME]

    j.update()

    j2 = Job.get(name=j.name)
    assert j2.title == j.title
    assert j2.employment_types == j.employment_types

    """ Search Query """
    job_query_obj = JobQuery(query="worker")
    request_metadata_obj = RequestMetadata(domain="pytalentsolution", session_id="1", user_id="tester")
    result = Job.search_jobs(tenant=tenant, job_query=job_query_obj, request_metadata=request_metadata_obj)
    assert result['matching_jobs'] is not None

    j.delete()

# def test_step_j(self):
#     """ Create client event """
#     client_obj = ClientEvent(event_id="1", create_time = "2020-10-24 10:00:00")
#     client_obj.event_notes = "test"
#     client_obj.request_id = "1"
#     result = create_client_event(tenant=tenant_obj, event= client_obj)
#     print(result)
#     self.assertIsNotNone(result, msg = "client event")

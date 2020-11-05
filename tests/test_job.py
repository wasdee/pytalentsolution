from uuid import uuid4

from pytalentsolution import CustomAttributes, EmploymentType, Job


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


    j.delete()
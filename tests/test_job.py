from uuid import uuid4

from pytalentsolution import (
                                CustomAttributes, 
                                EmploymentType, 
                                Job, 
                                JobQuery, 
                                RequestMetadata, 
                                CompensationInfo, 
                                CompensationEntry, 
                                CompensationRange,
                                Money,
                                DegreeType,
                                CTS_CompensationInfo,
                                # LocationFilters
                            )
# from google.cloud.talent_v4 import LocationFilters


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
                ),
                "min_exp": CustomAttributes(
                        long_values=[20],
                        filterable=True,
                        keyword_searchable=True
                )
            },
            addresses=["333/99 Moo 9, Pattaya Beach Road, South Pattaya, Chonburi, Thailand, 20150"],
            language_code="en-US",
            compensation_info=CompensationInfo(
                entries=[
                    CompensationEntry(
                        unit=CTS_CompensationInfo.CompensationUnit.MONTHLY,
                        range_=CompensationRange(
                            min_compensation=Money(
                                currency_code="THB", units=20000
                                ),
                            max_compensation=Money(
                                currency_code="THB", units=30000
                                )
                            ),
                        ),
                        ]
                    ),
            degree_types=[DegreeType.BACHELORS_OR_EQUIVALENT],
            )

    j3 = Job(
            company=company.name,
            requisition_id=uuid4().hex,
            title="worker",
            description="implement system",
            custom_attributes={
                "tags": CustomAttributes(
                        string_values=["hello"],
                        filterable=True,
                        keyword_searchable=True
                ),
                "min_exp": CustomAttributes(
                        long_values=[20],
                        filterable=True,
                        keyword_searchable=True
                )
            },
            addresses=["333/99 Moo 9, Pattaya Beach Road, South Pattaya, Chonburi, Thailand, 20150"],
            language_code="en-US",
            compensation_info=CompensationInfo(
                entries=[
                    CompensationEntry(
                        unit=CTS_CompensationInfo.CompensationUnit.MONTHLY,
                        range_=CompensationRange(
                            min_compensation=Money(
                                currency_code="THB", units=20000
                                ),
                            max_compensation=Money(
                                currency_code="THB", units=30000
                                )
                            ),
                        ),
                        ]
                    ),
            employment_types = [EmploymentType.PART_TIME],
            degree_types=[DegreeType.BACHELORS_OR_EQUIVALENT],
            )

    j4 = Job(
            company=company.name,
            requisition_id=uuid4().hex,
            title="worker",
            description="implement software",
            custom_attributes={
                "tags": CustomAttributes(
                        string_values=["hello"],
                        filterable=True,
                        keyword_searchable=True
                ),
                "min_exp": CustomAttributes(
                        long_values=[20],
                        filterable=True,
                        keyword_searchable=True
                )
            },
            addresses=["333/99 Moo 9, Pattaya Beach Road, South Pattaya, Chonburi, Thailand, 20150"],
            language_code="en-US",
            compensation_info=CompensationInfo(
                entries=[
                    CompensationEntry(
                        unit=CTS_CompensationInfo.CompensationUnit.MONTHLY,
                        range_=CompensationRange(
                            min_compensation=Money(
                                currency_code="THB", units=20000
                                ),
                            max_compensation=Money(
                                currency_code="THB", units=30000
                                )
                            ),
                        ),
                        ]
                    ),
            employment_types = [EmploymentType.PART_TIME],
            degree_types=[DegreeType.BACHELORS_OR_EQUIVALENT],
            )
    j4.create(tenant=tenant)
    j.create(tenant=tenant)
    j3.create(tenant=tenant)

    """ Update Job """
    j.title = "worker"
    j.employment_types = [EmploymentType.PART_TIME]
    j.custom_attributes.update({
                "tags_v1": CustomAttributes(
                        string_values=["hello"],
                        filterable=True,
                        keyword_searchable=True
                ),
                "min_exp_v2": CustomAttributes(
                        long_values=[20],
                        filterable=True,
                        keyword_searchable=True
                )})
    j.update()

    j2 = Job.get(name=j.name)
    assert j2.title == j.title
    assert j2.employment_types == j.employment_types


    """ Search Query """
    job_query_obj = JobQuery(
                        query="worker",
                        query_language_code= "en-US",
                        language_codes=["th-TH","en-US"],
                        location_filters=[{"address" : "chonburi","region_code":"TH"},{"address" : "bangkok","region_code":"TH"}],
                        employment_types=[EmploymentType.FULL_TIME]
                        )

    request_metadata_obj = RequestMetadata(domain="pytalentsolution", session_id="1", user_id="tester")
    result = Job.search_jobs(tenant=tenant, job_query=job_query_obj, request_metadata=request_metadata_obj)
    assert 'matching_jobs' not in result

    job_query_obj = JobQuery(
                        query="worker",
                        query_language_code= "en-US",
                        language_codes=["th-TH","en-US"],
                        location_filters=[{"address" : "bangkok","region_code":"TH"}],
                        employment_types=[EmploymentType.PART_TIME]
                        )

    request_metadata_obj = RequestMetadata(domain="pytalentsolution", session_id="1", user_id="tester")
    result = Job.search_jobs(tenant=tenant, job_query=job_query_obj, request_metadata=request_metadata_obj)
    assert 'matching_jobs' not in result

    job_query_obj = JobQuery(
                        query="worker",
                        query_language_code= "en-US",
                        language_codes=["th-TH","en-US"],
                        location_filters=[{"address" : "chonburi","region_code":"TH"}],
                        employment_types=[EmploymentType.PART_TIME]
                        )

    request_metadata_obj = RequestMetadata(domain="pytalentsolution", session_id="1", user_id="tester")
    result = Job.search_jobs(tenant=tenant, job_query=job_query_obj, request_metadata=request_metadata_obj)
    assert result['matching_jobs'] is not None

    job_query_obj = JobQuery(
                        query="worker",
                        query_language_code= "en-US",
                        language_codes=["th-TH","en-US"],
                        location_filters=[{"address" : "chonburi","region_code":"TH"}],
                        employment_types=[EmploymentType.PART_TIME]
                        )

    request_metadata_obj = RequestMetadata(domain="pytalentsolution", session_id="1", user_id="tester")
    result = Job.search_jobs(tenant=tenant, job_query=job_query_obj, request_metadata=request_metadata_obj)
    assert result['matching_jobs'] is not None

    job_query_obj = JobQuery(
                        query="worker",
                        query_language_code= "en-US",
                        language_codes=["th-TH","en-US"],
                        location_filters=[{"address" : "chonburi","region_code":"TH"}],
                        employment_types=[EmploymentType.PART_TIME]
                        )

    request_metadata_obj = RequestMetadata(domain="pytalentsolution", session_id="2", user_id="tester_2")
    result = Job.search_jobs(tenant=tenant, job_query=job_query_obj, request_metadata=request_metadata_obj)

    assert result['matching_jobs'] is not None

    j.delete()
    j3.delete()
    j4.delete()

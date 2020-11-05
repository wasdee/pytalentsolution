from pytalentsolution.job import CustomAttributes, Job


def test_job_with_custom_attribute():
    job = Job(
            company="codustry",
            requisition_id="codustry",
            title="codustry company",
            description="a tech company",
            custom_attributes={
                "sample": CustomAttributes(
                        string_values=["hello"],
                        keyword_searchable=True,
                )
            }
    )
    job.prepare_for_rpc()

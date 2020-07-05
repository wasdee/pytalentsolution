"""https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs"""
from pydantic import BaseModel


class Job(BaseModel):
    "name": string,
    "company": string,
    "requisitionId": string,
    "title": string,
    "description": string,
    "addresses": [
        string
    ],
    "applicationInfo": {
        object(ApplicationInfo)
    },
    "jobBenefits": [
        enum(JobBenefit)
    ],
    "compensationInfo": {
        object(CompensationInfo)
    },
    "customAttributes": {
        string: {
            object(CustomAttribute)
        },
        ...
    },
    "degreeTypes": [
        enum(DegreeType)
    ],
    "department": string,
    "employmentTypes": [
        enum(EmploymentType)
    ],
    "incentives": string,
    "languageCode": string,
    "jobLevel": enum(JobLevel),
    "promotionValue": number,
    "qualifications": string,
    "responsibilities": string,
    "postingRegion": enum(PostingRegion),
    "visibility": enum(Visibility),
    "jobStartTime": string,
    "jobEndTime": string,
    "postingPublishTime": string,
    "postingExpireTime": string,
    "postingCreateTime": string,
    "postingUpdateTime": string,
    "companyDisplayName": string,
    "derivedInfo": {
        object(DerivedInfo)
    },
    "processingOptions": {
        object(ProcessingOptions)
    }
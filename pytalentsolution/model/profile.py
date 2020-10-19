

from enum import auto
from typing import Optional, List, Any

from pydantic import BaseModel

from pytalentsolution.model.company import AutoName, Location
from pytalentsolution.model.job import DegreeType


class ResumeType(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#ResumeType
    """
    RESUME_TYPE_UNSPECIFIED = auto()
    HRXML = auto()
    OTHER_RESUME_TYPE = auto()


class Resume(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#Resume
    """
    structuredResume: Optional[str]
    resumeType: Optional[ResumeType]


class PersonStructuredName(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#PersonStructuredName
    """
    givenName: Optional[str]
    preferredName: Optional[str]
    middleInitial: Optional[str]
    familyName: Optional[str]
    suffixes: Optional[List[str]]
    prefixes: Optional[List[str]]


class PersonName(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#PersonName
    """
    preferredName: Optional[str]

    #Union field person_name can be only one of the following:
    formattedName: Optional[str]
    structuredName: Optional[PersonStructuredName]
    #End of list of possible types for union field person_name.


class ContactInfoUsage(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#ContactInfoUsage
    """
    CONTACT_INFO_USAGE_UNSPECIFIED = auto()
    PERSONAL = auto()
    WORK = auto()
    SCHOOL = auto()


class PostalAddress(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/PostalAddress
    """
    revision: Optional[int]
    regionCode: str
    languageCode: Optional[str]
    postalCode: Optional[str]
    sortingCode: Optional[str]
    administrativeArea: Optional[str]
    locality: Optional[str]
    sublocality: Optional[str]
    addressLines: Optional[List[str]]
    recipients: Optional[List[str]]
    organization: Optional[str]


class Address(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#Address
    """
    usage: Optional[ContactInfoUsage]
    current: Optional[bool]

    #Union field address can be only one of the following:
    unstructuredAddress: Optional[str]
    structuredAddress: Optional[PostalAddress]
    #End of list of possible types for union field address


class Email(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#Email
    """
    usage: Optional[ContactInfoUsage]
    emailAddress: Optional[str]


class PhoneType(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#PhoneType
    """
    PHONE_TYPE_UNSPECIFIED = auto()
    LANDLINE = auto()
    MOBILE = auto()
    FAX = auto()
    PAGER = auto()
    TTY_OR_TDD = auto()
    VOICEMAIL = auto()
    VIRTUAL = auto()
    VOIP = auto()
    MOBILE_OR_LANDLINE = auto()


class Phone(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#Phone
    """
    usage: Optional[ContactInfoUsage]
    type: Optional[PhoneType]
    number: Optional[str]
    whenAvailable: Optional[str]


class PersonalUri(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#PersonalUri
    """
    uri: Optional[str]


class AdditionalContactInfo(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#AdditionalContactInfo
    """
    usage: Optional[ContactInfoUsage]
    name: Optional[str]
    contactId: Optional[str]


class Date(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/Date
    """
    year: Optional[int]
    month: Optional[int]
    day: Optional[int]


class EmploymentRecord(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#EmploymentRecord
    """
    startDate: Optional[Date]
    endDate: Optional[Date]
    employerName: Optional[str]
    divisionName: Optional[str]
    address: Optional[Address]
    jobTitle: Optional[str]
    jobDescription: Optional[str]
    isSupervisor: Optional[bool]
    isSelfEmployed: Optional[bool]
    isCurrent: Optional[bool]

    #output
    jobTitleSnippet: Optional[str]
    jobDescriptionSnippet: Optional[str]
    employerNameSnippet: Optional[str]


class Degree(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#Degree
    """
    degreeType: Optional[DegreeType]
    degreeName: Optional[str]
    fieldsOfStudy: Optional[List[str]]


class EducationRecord(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#EducationRecord
    """
    startDate: Optional[Date]
    endDate: Optional[Date]
    expectedGraduationDate: Optional[Date]
    schoolName: Optional[str]
    address: Optional[Address]
    description: Optional[str]
    isCurrent: Optional[bool]

    #output
    schoolNameSnippet: Optional[str]
    degreeSnippet: Optional[str]

    #Union field degree can be only one of the following:
    degreeDescription: Optional[str]
    structuredDegree: Optional[Degree]
    #End of list of possible types for union field degree.


class SkillProficiencyLevel(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#SkillProficiencyLevel
    """
    SKILL_PROFICIENCY_LEVEL_UNSPECIFIED = auto()
    UNSKILLED = auto()
    FUNDAMENTAL_AWARENESS = auto()
    NOVICE = auto()
    INTERMEDIATE = auto()
    ADVANCED = auto()
    EXPERT = auto()


class Skill(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#Skill
    """
    displayName: Optional[str]
    lastUsedDate: Optional[Date]
    level: Optional[SkillProficiencyLevel]
    context: Optional[str]

    #output
    skillNameSnippet: Optional[str]


class Activity(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#Activity
    """
    displayName: Optional[str]
    description: Optional[str]
    uri: Optional[str]
    createDate: Optional[Date]
    updateDate: Optional[Date]
    teamMembers: Optional[List[str]]
    skillsUsed: Optional[List[Skill]]

    #output
    activityNameSnippet: Optional[str]
    activityDescriptionSnippet: Optional[str]
    skillsUsedSnippet: Optional[List[str]]


class Publication(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#Publication
    """
    authors: Optional[List[str]]
    title: Optional[str]
    description: Optional[str]
    journal: Optional[str]
    volume: Optional[str]
    publisher: Optional[str]
    publicationDate: Optional[Date]
    publicationType: Optional[str]
    isbn: Optional[str]


class Patent(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#Patent
    """
    displayName: Optional[str]
    inventors: Optional[List[str]]
    patentStatus: Optional[str]
    patentStatusDate: Optional[Date]
    patentFilingDate: Optional[Date]
    patentOffice: Optional[str]
    patentNumber: Optional[str]
    patentDescription: Optional[str]
    skillsUsed: Optional[List[Skill]]


class Certification(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#Certification
    """
    displayName: Optional[str]
    acquireDate: Optional[Date]
    expireDate: Optional[Date]
    authority: Optional[str]
    description: Optional[str]


class AvailabilitySignalType(AutoName):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#availabilitysignaltype
    """
    AVAILABILITY_SIGNAL_TYPE_UNSPECIFIED = auto()
    JOB_APPLICATION = auto()
    RESUME_UPDATE = auto()
    CANDIDATE_UPDATE = auto()
    CLIENT_SUBMISSION = auto()


class AvailabilitySignal(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles#availabilitysignal
    """
    type: Optional[AvailabilitySignalType]
    lastUpdateTime: Optional[str]
    filterSatisfied: Optional[bool]


class Profile(BaseModel):
    """
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.tenants.profiles
    """
    name: str
    externalId: Optional[str]
    source: Optional[str]
    uri: Optional[str]
    groupId: Optional[str]
    isHirable: Optional[bool]
    createTime: Optional[str]
    updateTime: Optional[str]
    candidateUpdateTime: Optional[str]
    resumeUpdateTime: Optional[str]
    resume: Optional[Resume]
    personNames: Optional[List[PersonName]]
    addresses: Optional[List[Address]]
    emailAddresses: Optional[List[Email]]
    phoneNumbers: Optional[List[Phone]]
    personalUris: Optional[List[PersonalUri]]
    additionalContactInfo: Optional[List[AdditionalContactInfo]]
    employmentRecords: Optional[List[EmploymentRecord]]
    educationRecords: Optional[List[EducationRecord]]
    skills: Optional[List[Skill]]
    activities: Optional[List[Activity]]
    publications: Optional[List[Publication]]
    patents: Optional[List[Patent]]
    certifications: Optional[List[Certification]]

    #output only
    applications: Optional[List[str]]
    assignments: Optional[List[str]]
    customAttributes: Optional[Any]
    # customAttributes: Optional[{
    #     str
    #     : {
    #         object(CustomAttribute)
    #     },
    #     ...
    # },
    processed: Optional[bool]
    keywordSnippet: Optional[str]
    availabilitySignals: Optional[List[AvailabilitySignal]]
    derivedAddresses: Optional[List[Location]]
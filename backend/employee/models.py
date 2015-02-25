from django.db import models
from django.conf import settings
from common.models import(
    AbstractBase,
    Location,
    Job,
    Skill,
    Industry
)


class Employee(AbstractBase):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    location = models.ForeignKey(Location)
    phone_number = models.CharField(max_length=128, null=False, blank=False)
    skills = models.ManyToManyField(Skill)
    industry = models.ManyToManyField(Industry)


class AppliedJobs(AbstractBase):
    employee = models.ForeignKey(Employee)
    job = models.ForeignKey(Job)

from django.db import models
from django.conf import settings
from common.models import(
    AbstractBase,
    Location,
    Job
)


class Employer(AbstractBase):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    location = models.ForeignKey(Location)
    phone_number = models.CharField(max_length=128, null=False, blank=False)

    @property
    def employer_location(self):
        return self.location.name


class EmployerJobs(AbstractBase):
    employer = models.ForeignKey(Employer)
    job = models.ForeignKey(Job)

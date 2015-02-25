from django.db import models
from django.utils import timezone


class AbstractBase(models.Model):
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Location(AbstractBase):
    name = models.CharField(max_length=128, null=False, blank=False)

    def __unicode__(self):
        return self.name


class Industry(AbstractBase):
    name = models.CharField(
        max_length=128, null=False, blank=False, unique=True)

    def __unicode__(self):
        return self.name


class Skill(AbstractBase):
    name = models.CharField(
        max_length=128, null=False,
        blank=False, unique=True)

    def __unicode__(self):
        return self.name


class Job(AbstractBase):
    name = models.CharField(max_length=128, null=False, blank=False)
    start_date = models.DateTimeField(default=timezone.now)
    expires_on = models.DateTimeField(null=False, blank=False)
    is_active = models.BooleanField(default=True)
    industry = models.ForeignKey(Industry, related_name='industry')
    skills = models.ManyToManyField(Skill, related_name='skills')
    location = models.ForeignKey(Location)

    """
        Todo:
        validate expires_on > start_date
        automatically set is_active=False when now()==expires_on
    """

from django.db import models
from django.utils import timezone


class AbstractBase(models.Model):
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Location(AbstractBase):
    name = models.CharField(max_length=128, null=False, blank=False)


class Industry(AbstractBase):
    name = models.CharField(max_length=128, null=False, blank=False)


class Skill(AbstractBase):
    name = models.CharField(max_length=128, null=False, blank=False)

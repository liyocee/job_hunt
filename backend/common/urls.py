from django.conf.urls import url, patterns
from .views import (IndustryView, LocationView, SkillView)


urlpatterns = patterns(
    '',
    url(r'^industry/$', IndustryView.as_view(), name="industry"),
    url(r'^location/$', LocationView.as_view(), name="location"),
    url(r'^skill/$', SkillView.as_view(), name="skill")
)

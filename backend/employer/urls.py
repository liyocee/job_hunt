from django.conf.urls import url, patterns
from .views import (EmployerView, EmployerJobsView)


urlpatterns = patterns(
    '',
    url(r'^$', EmployerView.as_view(), name="employer"),
    url(r'^jobs/$', EmployerJobsView.as_view(), name="employer_jobs")
)

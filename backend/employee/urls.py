from django.conf.urls import url, patterns
from .views import (EmployeeView, AppliedJobsView, JobMatchesView)


urlpatterns = patterns(
    '',
    url(r'^$', EmployeeView.as_view(), name="employee"),
    url(r'^jobs/$', AppliedJobsView.as_view(), name="employee_jobs"),
    url(r'^job_matches/$', JobMatchesView.as_view(), name="job_matches")
)

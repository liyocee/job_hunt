from django.conf.urls import url, patterns
from .views import (EmployeeView, AppliedJobsView)


urlpatterns = patterns(
    '',
    url(r'^$', EmployeeView.as_view(), name="employee"),
    url(r'^jobs/$', AppliedJobsView.as_view(), name="employee_jobs")
)

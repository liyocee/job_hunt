from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from employer.serializers import EmployerJobsSerializer
from common.models import Job
from .serializers import EmployeeSerializer, AppliedJobsSerializer
from .models import Employee, AppliedJobs
from .job_match import JobMatch


class EmployeeView(generics.ListCreateAPIView):
    permission_class = (AllowAny, )
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class AppliedJobsView(generics.ListCreateAPIView):
    permission_class = (AllowAny, )
    serializer_class = AppliedJobsSerializer
    queryset = AppliedJobs.objects.all()


class JobMatchesView(generics.ListAPIView):
    permission_class = (IsAuthenticated, )
    serializer_class = EmployerJobsSerializer

    def get_queryset(self):
        try:
            employee = Employee.objects.get(user=self.request.user)
            return JobMatch(employee, Job.objects.all()).matches()
        except Employee.DoesNotExist:
            return []

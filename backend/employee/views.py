from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import EmployeeSerializer, AppliedJobsSerializer
from .models import Employee, AppliedJobs


class EmployeeView(generics.ListCreateAPIView):
    permission_class = (AllowAny, )
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class AppliedJobsView(generics.ListCreateAPIView):
    permission_class = (AllowAny, )
    serializer_class = AppliedJobsSerializer
    queryset = AppliedJobs.objects.all()

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import EmployerSerializer, EmployerJobsSerializer
from .models import Employer, EmployerJobs


class EmployerView(generics.ListCreateAPIView):
    permission_class = (AllowAny, )
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()


class EmployerJobsView(generics.ListCreateAPIView):
    permission_class = (IsAuthenticated, )
    serializer_class = EmployerJobsSerializer
    queryset = EmployerJobs.objects.all()

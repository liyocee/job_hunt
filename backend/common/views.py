from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    LocationSerializer, IndustrySerializer, SkillSerializer)
from .models import Location, Industry, Skill


class IndustryView(generics.ListCreateAPIView):
    permission_class = (IsAuthenticated, )
    serializer_class = IndustrySerializer
    queryset = Industry.objects.all()


class SkillView(generics.ListCreateAPIView):
    permission_class = (IsAuthenticated, )
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class LocationView(generics.ListCreateAPIView):
    permission_class = (IsAuthenticated, )
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

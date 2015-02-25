from rest_framework import serializers
from .models import (Job)


class JobSerializer(serializers.ModelSerializer):
    industry_details = serializers.SerializerMethodField()
    location_details = serializers.SerializerMethodField()
    skills_details = serializers.SerializerMethodField()

    def get_industry_details(self, obj):
        return obj.industry.name

    def get_location_details(self, obj):
        return obj.location.name

    def get_skills_details(self, obj):
        return obj.skills.values()

    class Meta:
        model = Job

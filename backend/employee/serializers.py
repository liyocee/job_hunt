from rest_framework import serializers
from django.contrib.auth import get_user_model
from job_auth.serializers import UserSerializer
from common.serializers import JobSerializer
from .models import Employee, AppliedJobs


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    industry_details = serializers.SerializerMethodField()
    location_details = serializers.SerializerMethodField()
    skills_details = serializers.SerializerMethodField()

    def get_industry_details(self, obj):
        return obj.industry.values()

    def get_location_details(self, obj):
        return obj.location.name

    def get_skills_details(self, obj):
        return obj.skills.values()

    def create(self, validated_data):
        try:
            user = get_user_model().objects.get(
                username=validated_data['user']['username'])
        except get_user_model().DoesNotExist:
            user = get_user_model().objects.create(**validated_data['user'])
        validated_data['user'] = user
        return super(EmployeeSerializer, self).create(validated_data)

    class Meta:
        model = Employee


class AppliedJobsSerializer(serializers.ModelSerializer):
    employee_details = serializers.SerializerMethodField()
    job_details = serializers.SerializerMethodField()

    def get_employee_details(self, obj):
        return EmployeeSerializer(obj.employee).data

    def get_job_details(self, obj):
        return JobSerializer(obj.job).data

    class Meta:
        model = AppliedJobs

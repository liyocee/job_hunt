from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from common.serializers import JobSerializer
from job_auth.serializers import UserSerializer
from .models import(
    Employer,
    EmployerJobs
)


class EmployerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    employer_location = serializers.CharField(read_only=True)

    def create(self, validated_data):
        try:
            user = get_user_model().objects.get(
                username=validated_data['user']['username'])
        except get_user_model().DoesNotExist:
            user = get_user_model().objects.create(**validated_data['user'])
        validated_data['user'] = user
        return super(EmployerSerializer, self).create(validated_data)

    class Meta:
        model = Employer


class EmployerJobsSerializer(serializers.ModelSerializer):
    job = JobSerializer(required=True)
    employer_details = serializers.SerializerMethodField()

    def create(self, validated_data):
        job = self.initial_data['job']
        job_serializer = JobSerializer(data=job)
        if job_serializer.is_valid():
            job_obj = job_serializer.save()
            validated_data['job'] = job_obj
            return super(EmployerJobsSerializer, self).create(validated_data)
        else:
            raise ValidationError(job_serializer.errors)

    def get_employer_details(self, obj):
        return EmployerSerializer(obj.employer).data

    class Meta:
        model = EmployerJobs

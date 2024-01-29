from rest_framework import serializers

from edu.models import Course


# from models import


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['pk', 'name', 'description', 'price', 'estimate_days', 'difficulty', 'file_url']

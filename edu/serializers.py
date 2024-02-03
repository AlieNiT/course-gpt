from rest_framework import serializers

from edu.models import Course, User


# from models import


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['pk', 'name', 'description', 'price', 'estimate_days', 'difficulty', 'file_url']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'email','type', 'balance']

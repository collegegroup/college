from ..models import BasicCoachingCourses
from rest_framework import serializers
__author__ = 'ravi'


class BasicCoachingCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicCoachingCourses()
        fields = ['course_name', 'category_name']
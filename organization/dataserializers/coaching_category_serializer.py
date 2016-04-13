from ..models import BasicCoachingCourses
from rest_framework import serializers


class BasicCoachingCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicCoachingCourses()
        fields = ['course_name', 'category_name']
from ..models import BasicCollegeCourses
from rest_framework import serializers


class BasicCollegeCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicCollegeCourses()
        fields = ['course_name', 'category_name']
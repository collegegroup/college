from ..models import BasicCollegeCourses
from rest_framework import serializers
__author__ = 'ravi'


class BasicCollegeCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicCollegeCourses()
        fields = ['course_name', 'category_name']
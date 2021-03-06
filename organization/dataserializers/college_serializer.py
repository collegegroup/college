from ..models import CollegeMain, CollegeCourses
from rest_framework import serializers
__author__ = 'ravi'


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeMain()
        fields = ['school_id', 'school_name', 'location', 'establishment', 'description', 'affiliation',
                  'website', 'address', 'landline_num', 'mobile_num', 'emailid']


class CollegeSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeMain()
        fields = ['college_id', 'college_name']


class CollegeCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeCourses()
        fields = ['course']

from ..models import CollegeMain, CollegeCourses, CollegeFacilities
from rest_framework import serializers
__author__ = 'ravi'


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeMain()
        fields = ['college_name', 'establishment', 'description', 'affiliation',
                  'website', 'address', 'landline_num', 'mobile_num', 'emailid', 'highest_package',
                  'average_package', 'city_name', 'state_name']


class CollegeSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeMain()
        fields = ['college_id', 'college_name']


class CollegeCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeCourses()
        fields = ['course']


class CollegeFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeFacilities
        fields = ['facility_name']


class CollegeFullCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeCourses()
        fields = ['course', 'duration', 'fee', 'entrance']

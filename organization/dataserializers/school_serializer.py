from ..models import SchoolMain
from rest_framework import serializers
__author__ = 'ravi'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolMain()
        fields = ['school_id', 'school_name', 'location', 'establishment', 'description', 'affiliation',
                  'website', 'address', 'landline_num', 'mobile_num', 'emailid']


class SchoolSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolMain()
        fields = ['school_id', 'school_name']
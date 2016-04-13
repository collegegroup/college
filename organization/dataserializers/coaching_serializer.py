from ..models import InstituteMain
from rest_framework import serializers


class CoachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteMain()
        fields = ['institute_id', 'institute_name', 'location', 'establishment', 'description', 'affiliation',
                  'website', 'address', 'landline_num', 'mobile_num', 'emailid']


class CoachingSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteMain()
        fields = ['institute_id', 'institute_name']
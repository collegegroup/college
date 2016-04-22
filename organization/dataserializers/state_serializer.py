from ..models import *
from rest_framework import serializers
__author__ = 'ravi'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State()
        fields = ['state_name']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location()
        fields = ['state_name', 'city_name', 'sub_city', 'pin_code', 'status']

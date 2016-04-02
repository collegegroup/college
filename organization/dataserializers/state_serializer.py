from ..models import *
from rest_framework import serializers


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State()
        fields = 'state_name'

from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from ..location_services import LocationORM
from ..dataserializers.state_serializer import *
import json


class AddState(APIView):
    def post(self, request):
        if request.method == 'POST':
            response = dict()
            state_name = request.POST.get('state_name')
            if not LocationORM.is_state_exists(state_name):
                try:
                    LocationORM.add_state(state_name)
                    response.update({'message': 'data saved successfully'})
                    response.update({'status': 'success'})
                    response.update({'response_code': status.HTTP_200_OK})
                except:
                    response.update({'message': 'could not saved data'})
                    response.update({'status': 'error'})
                    response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
            else:
                response.update({'message': 'could not saved data'})
                response.update({'status': 'state already exits'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
            return HttpResponse(json.dumps(response), content_type="application/json")


class GetState(APIView):

    def get(self, request):
        if request.method == 'GET':
            response = dict()
            try:
                states = LocationORM.get_all_state()
                state_serializer = StateSerializer(states, many=True)
                response.update({'data': state_serializer.data})
                response.update({'status': 'success'})
                response.update({'response_code': status.HTTP_200_OK})
            except Exception as ex:
                response.update({'message': 'could not get data'})
                response.update({'status': 'error'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
            return HttpResponse(json.dumps(response), content_type="application/json")


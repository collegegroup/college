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

            try:
                LocationORM.add_state(state_name)
                response.update({'message': 'data saved successfully'})
                response.update({'status': 'success'})
                response.update({'response_code': status.HTTP_200_OK})
            except:
                response.update({'message': 'could not saved data'})
                response.update({'status': 'error'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})

            return HttpResponse(json.dumps(response), content_type="application/json")


class GetAllState(APIView):

    def get(self, request):
        if request.method == 'GET':
            response = dict()
            try:
                states = LocationORM.get_all_state()
                # state_serializer = StateSerializer(states, many=True)
                states_list = list()
                for state in states:
                    # states_dict.update({'state_id': state.state_id, 'state_name': state.state_name})
                    states_list.append(state.state_name)
                response.update({'data': {'states': states_list}})
                response.update({'status': 'success'})
                response.update({'response_code': status.HTTP_200_OK})
            except Exception as ex:
                response.update({'message': 'could not get data'})
                response.update({'status': 'error'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
            return HttpResponse(json.dumps(response), content_type="application/json")


class AddCity(APIView):
    def post(self, request):
        if request.method == 'POST':
            response = dict()
            state_name = request.POST.get('state_name')
            city_name = request.POST.get('city_name')

            try:
                LocationORM.add_city(city_name, state_name)
                response.update({'message': 'data saved successfully'})
                response.update({'status': 'success'})
                response.update({'response_code': status.HTTP_200_OK})
            except Exception as ex:
                response.update({'message': 'could not saved data'})
                response.update({'status': 'error'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})

            return HttpResponse(json.dumps(response), content_type="application/json")


class GetAllCity(APIView):

    def get(self, request):
        if request.method == 'GET':
            response = dict()
            try:
                cities = LocationORM.get_all_city()
                # state_serializer = StateSerializer(states, many=True)
                city_list = list()
                for city in cities:
                    city_list.append(city.city_name)

                response.update({'data': {'cities': city_list}})
                response.update({'status': 'success'})
                response.update({'response_code': status.HTTP_200_OK})
            except Exception as ex:
                response.update({'message': 'could not get data'})
                response.update({'status': 'error'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
            return HttpResponse(json.dumps(response), content_type="application/json")


class AddLocation(APIView):
    def post(self, request):
        if request.method == 'POST':
            response = dict()
            state_name = request.POST.get('state_name')
            city_name = request.POST.get('city_name')
            pin_code = request.POST.get('pin_code')
            sub_city = request.POST.get('location_name')

            try:
                LocationORM.add_location(state_name, city_name, sub_city, pin_code)
                response.update({'message': 'data saved successfully'})
                response.update({'status': 'success'})
                response.update({'response_code': status.HTTP_200_OK})
            except Exception as ex:
                response.update({'message': 'could not saved data'})
                response.update({'status': 'error'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})

            return HttpResponse(json.dumps(response), content_type="application/json")


class GetLocation(APIView):
    def get(self, request):
        if request.method == 'GET':
            response = dict()
            try:
                locations = LocationORM.get_all_location()
                location_serializer = LocationSerializer(locations, many=True)
                response.update({'data': {'locations': location_serializer.data}})
                response.update({'status': 'success'})
                response.update({'response_code': status.HTTP_200_OK})
            except Exception as ex:
                response.update({'message': 'could not get data'})
                response.update({'status': 'error'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
            return HttpResponse(json.dumps(response), content_type="application/json")
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from django.core.files.base import ContentFile
from ..school_services import SchoolOrm
from ..jsonparser.school_jsons import *
import json
# Create your views here.


class SchoolRegister(APIView):

    def post(self, request):
        if request.method == 'POST':
            school_json_parser = SchoolJsonParser()
            '''
            school_name = request.POST.get('school_name')
            location = request.POST.get('location')
            establishment = request.POST.get('establishment')
            description = request.POST.get('description')
            affiliation = request.POST.get('affiliation')
            website = request.POST.get('website')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            address = request.POST.get('address')
            landline_num = request.POST.get('landline_num')
            mobile_num = request.POST.get('mobile_num')
            emailid = request.POST.get('emailid')

            school_helper = SchoolHelper(school_name, location, establishment, description, affiliation, website,
                                         start_time, end_time, address, landline_num, mobile_num, emailid, '')
            '''
            school_helper = school_json_parser.school_register_json_parser(request.body)
            school_orm = SchoolOrm()
            response = dict()
            try:
                school_orm.save_school(school_helper)
                response.update({'message': 'date saved successfully!'})
            except Exception as ex:
                response.update({'message': ex})

            return HttpResponse(json.dumps(response), content_type="application/json")


class UploadSchoolProfile(APIView):

    def post(self, request):
        if request.method == 'POST':
            response = dict()
            school_main = SchoolOrm.get_school_by_id(request.POST.get('school_id'))
            image_name = "profile_" + str(school_main.school_id) + ".jpg"
            image = ContentFile(request.FILES['image'].read())
            try:
                school_main.profile_image.save(image_name, image)
                response.update({'message': 'profile picture uploaded successfully!'})
                response.update({'profile_name': '/media/' + str(school_main.profile_image)})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                response.update({'message': ex})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})
            return HttpResponse(json.dumps(response), content_type="application/json")
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from django.core.files.base import ContentFile
from ..school_services import SchoolOrm
from ..core import *
from django.conf import settings
from ..jsonparser.school_jsons import *
import json, uuid
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
            image_name = settings.MEDIA_ROOT + "profiles/school/profile_" + str(uuid.uuid4()) + ".jpg"
            try:
                handle_uploaded_file(request.FILES['file'], image_name)
                response.update({'message': 'profile picture uploaded successfully!'})
                response.update({'profile_image_path': '/' + image_name})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                response.update({'message': ex})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})
            return HttpResponse(json.dumps(response), content_type="application/json")
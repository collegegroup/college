from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from ..college_services import CollegeOrm, CollegeCourseOrm, FacilitiesORM
from ..jsonparser.college_jsons import *
from ..core import *
from django.conf import settings
import json, uuid
from ..models import CollegeMain
from django.core.files.base import ContentFile
# Create your views here.


class CollegeRegister(APIView):

    def post(self, request):
        if request.method == 'POST':
            college_json_parser = CollegeJsonParser()
            college_helper, courses, facilities = college_json_parser.college_register_json_parser(request.body)
            college_orm = CollegeOrm()
            response = dict()
            try:
                college_id = college_orm.save_college(college_helper)
                for course in courses:
                    CollegeCourseOrm.save_college_course(course, college_id)
                for facility in facilities:
                    FacilitiesORM.save_facility(college_id, facility)
                response.update({'message': 'date saved successfully!'})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                print (ex)
                response.update({'message': 'could not save data'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})
            return HttpResponse(json.dumps(response), content_type="application/json")


class UploadCollegeProfile(APIView):

    def post(self, request):
        if request.method == 'POST':
            response = dict()
            image_name = settings.MEDIA_ROOT + "profiles/college/profile_" + str(uuid.uuid4()) + ".jpg"
            try:
                handle_uploaded_file(request.FILES['file'], image_name)
                response.update({'message': 'profile picture uploaded successfully!'})
                response.update({'profile_image_path': '/' + image_name})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                response.update({'message': 'could not upload image'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})
            return HttpResponse(json.dumps(response), content_type="application/json")


from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from django.core.files.base import ContentFile
from ..school_services import SchoolOrm, FacilitiesORM, CurriculumORM
from ..core import *
from django.conf import settings
from ..jsonparser.school_jsons import *
import json, uuid
# Create your views here.


class SchoolRegister(APIView):

    def post(self, request):
        if request.method == 'POST':
            school_json_parser = SchoolJsonParser()
            school_helper, facilities, extra_curriculum = school_json_parser.school_register_json_parser(request.body)
            school_orm = SchoolOrm()
            response = dict()
            try:
                school_id = school_orm.save_school(school_helper)
                for facility in facilities:
                    FacilitiesORM.save_facility(school_id, facility)
                for curriculum in extra_curriculum:
                    CurriculumORM.save_curriculum(school_id, curriculum)
                response.update({'message': 'date saved successfully!'})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                response.update({'message': 'could not save data'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})

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
                response.update({'message': 'could not upload image'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})
            return HttpResponse(json.dumps(response), content_type="application/json")
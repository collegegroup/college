from __future__ import print_function
from django.core.files.base import ContentFile
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from ..coaching_services import InstituteOrm, InstituteCourseOrm, FacilitiesORM, CategoryORM
from ..jsonparser.coaching_jsons import *
from ..core import *
from django.conf import settings
import json
import uuid


# Create your views here.


class CoachingRegister(APIView):
    def post(self, request):
        if request.method == 'POST':
            institute_orm = InstituteOrm()
            institute_json_parser = InstituteJsonParser()
            # print(request.POST.get('jsonData'))
            institute_helper, courses, facilities = institute_json_parser.institute_register_json_parser(request.POST.get('jsonData'))
            response = dict()

            try:
                institute_id = institute_orm.save_institute(institute_helper)
                for course in courses:
                    InstituteCourseOrm.save_institute_course(course, institute_id)
                for facility in facilities:
                    FacilitiesORM.save_facility(institute_id, facility)
                response.update({'message': 'date saved successfully!'})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                print (ex)
                response.update({'message': 'could not save data'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})

            # response.update({'jsonData': request.POST.get('jsonData')})
            return HttpResponse(json.dumps(response), content_type="application/json")


class UploadCoachingProfileTmp(APIView):
    def post(self, request):
        if request.method == 'POST':
            response = dict()
            institute_main = InstituteOrm.get_institute_by_id(request.POST.get('institute_id'))
            image_name = "profile_" + str(institute_main.institute_id) + ".jpg"
            image = ContentFile(request.FILES['image'].read())
            try:
                institute_main.profile_image.save(image_name, image)
                response.update({'message': 'profile picture uploaded successfully!'})
                response.update({'profile_name': '/media/' + str(institute_main.profile_image)})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                response.update({'message': ex})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})
            return HttpResponse(json.dumps(response), content_type="application/json")


class UploadCoachingProfile(APIView):
    def post(self, request):
        if request.method == 'POST':
            response = dict()
            image_name = settings.MEDIA_ROOT + "profiles/coaching/profile_" + str(uuid.uuid4()) + ".jpg"
            # image = ContentFile(request.FILES['image'].read())
            try:
                # institute_main.profile_image.save(image_name, image)
                handle_uploaded_file(request.FILES['file'], image_name)
                response.update({'message': 'profile picture uploaded successfully!'})
                response.update({'profile_image_path': "/" + image_name})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                response.update({'message': 'could not upload image'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})
            return HttpResponse(json.dumps(response), content_type="application/json")


class GetAllCoachingCategory(APIView):

    def get(self, request):
        if request.method == 'GET':
            response = dict()
            try:
                categories = CategoryORM.get_all_coaching_category()
                category_list = list()
                for category in categories:
                    category_list.append(category.category_name)
                response.update({'data': {'categories': category_list}})
                response.update({'status': 'success'})
                response.update({'response_code': status.HTTP_200_OK})
            except Exception as ex:
                response.update({'message': 'could not get data'})
                response.update({'status': 'error'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
            return HttpResponse(json.dumps(response), content_type="application/json")


class AddCoachingBasicCourses(APIView):
    def post(self, request):
        if request.method == 'POST':
            response = dict()
            category_name = request.POST.get('category_name')
            course_name = request.POST.get('course_name')

            try:
                CategoryORM.add_basic_course(category_name, course_name)
                response.update({'message': 'data saved successfully'})
                response.update({'status': 'success'})
                response.update({'response_code': status.HTTP_200_OK})
            except Exception as ex:
                response.update({'message': 'could not saved data'})
                response.update({'status': 'error'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})

            return HttpResponse(json.dumps(response), content_type="application/json")
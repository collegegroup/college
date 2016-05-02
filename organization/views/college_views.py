from __future__ import print_function
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from ..college_services import CollegeOrm, CollegeCourseOrm, FacilitiesORM, CategoryORM
from ..dataserializers.college_category_serializer import BasicCollegeCoursesSerializer
from ..dataserializers.college_serializer import CollegeCoursesSerializer
from ..jsonparser.college_jsons import *
from ..core import *
from django.conf import settings
import json, uuid
from ..models import *
from django.core.files.base import ContentFile
__author__ = 'ravi'
# Create your views here.


class CollegeRegister(APIView):

    def post(self, request):
        if request.method == 'POST':
            # print (request.POST.get('jsonData'))
            college_json_parser = CollegeJsonParser()
            college_helper, courses, facilities = college_json_parser.college_register_json_parser(request.POST.get('jsonData'))
            college_orm = CollegeOrm()
            response = dict()
            try:
                college_id = college_orm.save_college(college_helper)
                for course in courses:
                    CollegeCourseOrm.save_college_course(course, college_id)
                for facility in facilities:
                    FacilitiesORM.save_facility(college_id, facility)
                response.update({'message': 'data saved successfully!'})
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


class GetAllCollegeCategory(APIView):

    def get(self, request):
        if request.method == 'GET':
            response = dict()
            try:
                categories = CategoryORM.get_all_college_category()
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


class AddCollegeBasicCourses(APIView):
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


class GetAllBasicCollegeCourses(APIView):
    def get(self, request):
        if request.method == "GET":
            response = dict()
            try:
                basic_categories = CategoryORM.get_basic_category_and_course()

                response.update({'data': {'categories_courses': BasicCollegeCoursesSerializer(basic_categories,
                                                                                              many=True).data}})
                response.update({'status': 'success'})
                response.update({'response_code': status.HTTP_200_OK})
            except Exception as ex:
                response.update({'message': 'could not get data'})
                response.update({'status': 'error'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})

            return HttpResponse(json.dumps(response), content_type="application/json")


class GetCollegeForReview(APIView):
    def get(self, request, college_id):
        if request.method == "GET":
            response = dict()
            try:
                college = CollegeOrm.get_college_by_id(college_id)
                courses = CollegeCourseOrm.get_college_courses_by_id(college_id)
                response.update({'data': {'courses': CollegeCoursesSerializer(courses, many=True).data,
                                          'college_name': college.college_name}})
                response.update({'status': 'success'})
                response.update({'response_code': status.HTTP_200_OK})
            except Exception as ex:
                response.update({'message': 'could not get data'})
                response.update({'status': 'error'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})

            return HttpResponse(json.dumps(response), content_type="application/json")
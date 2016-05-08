from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from ..college_services import CollegeOrm, CollegeCourseOrm, FacilitiesORM
from ..college_review_services import CollegeReviewORM
from ..dataserializers.college_serializer import CollegeSerializer, CollegeFullCoursesSerializer,\
    CollegeFacilitiesSerializer
import json
__author__ = 'ravi'


class GetCollegeDetails(APIView):
    def get(self, request, college_id):
        if request.method == "GET":
            response = dict()
            try:
                college = CollegeOrm.get_college_by_id(college_id)
                courses = CollegeCourseOrm.get_college_courses_by_id(college_id)
                facilities = FacilitiesORM.get_facility(college_id)
                college_review_count = CollegeReviewORM.get_college_review_count(college_id)
                categories = list()
                for course in courses:
                    if course.category not in categories:
                        categories.append(course.category)
                courses_dict = list()
                for category in categories:
                    course_list = list()
                    for course in courses:
                        if course.category == category:
                            course_list.append(CollegeFullCoursesSerializer(course).data)
                    courses_dict.append({'category_name': category, 'category_courses': course_list})
                # CollegeCoursesSerializer(courses, many=True).data
                response.update({'data': {'courses': courses_dict,
                                          'college_details': CollegeSerializer(college, many=False).data,
                                          'facilities': CollegeFacilitiesSerializer(facilities, many=True).data,
                                          'college_review_details': {'review_count': college_review_count,
                                                                     'rating_count': college_review_count}}
                                 })
                response.update({'status': 'success'})
                response.update({'response_code': status.HTTP_200_OK})
            except Exception as ex:
                print (ex)
                response.update({'message': 'could not get data'})
                response.update({'status': 'error'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})

            return HttpResponse(json.dumps(response), content_type="application/json")
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from ..college_review_services import CollegeReviewORM
from ..college_services import CollegeOrm, CollegeCourseOrm
from ..dataserializers.college_serializer import CollegeSerializer
import json
__author__ = 'ravi'
# Create your views here.


class SearchColleges(APIView):
    def post(self, request):
        if request.method == "POST":
            college_list = list()
            response = dict()
            college_review_details = None
            state_name = request.POST.get('state')
            city_name = request.POST.get('city')
            course = request.POST.get('course')
            fee = request.POST.get('fee')
            try:
                colleges = CollegeOrm.get_college_by_state_city(state_name, city_name)
                print (len(colleges))
                for college in colleges:
                    college_course = CollegeCourseOrm.get_college_by_course(college.college_id, course, fee)
                    if college_course:
                        college_review_count = CollegeReviewORM.get_college_review_count(college_course.college_id)
                        if college_review_count:
                            college_review_details = {'review_count': college_review_count,
                                                      'rating_count': college_review_count}
                        else:
                            college_review_details = {'review_count': 0,
                                                      'rating_count': 0}
                        return_dict = CollegeSerializer(college, many=False).data
                        return_dict.update({'fee': str(college_course.fee), 'course': college_course.course,
                                            'college_review_details': college_review_details})
                        college_list.append(return_dict)
                response.update({'data': {'colleges': college_list}})
                response.update({'status': 'success'})
                response.update({'response_code': status.HTTP_200_OK})
            except Exception as ex:
                print (ex)
                response.update({'message': 'could not get data'})
                response.update({'status': 'error'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})

            return HttpResponse(json.dumps(response), content_type="application/json")

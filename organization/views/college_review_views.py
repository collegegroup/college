from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from ..jsonparser.college_review_json import CollegeReviewJsonParser
from ..college_review_services import CollegeReviewORM
import json
__author__ = 'ravi'


class AddCollegeReview(APIView):

    def post(self, request):
        if request.method == "POST":
            response = dict()
            try:
                college_review_helper = CollegeReviewJsonParser.college_review_json_parser(request.POST.get('jsonData'))
                CollegeReviewORM.save_college_review(college_review_helper)
                response.update({'message': "date saved successfully"})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                response.update({'message': 'could not save data'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})

            return HttpResponse(json.dumps(response), content_type="application/json")
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from ..jsonparser.school_review_json import SchoolReviewJsonParser
from ..school_review_services import SchoolReviewORM
import json
__author__ = 'ravi'

# Create your views here.


class AddSchoolReview(APIView):

    def post(self, request):
        if request.method == "POST":
            response = dict()
            try:
                school_review_helper = SchoolReviewJsonParser.school_review_json_parser(request.POST.get('jsonData'))
                SchoolReviewORM.save_school_review(school_review_helper)
                response.update({'message': "date saved successfully"})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                print ("error is ", ex)
                response.update({'message': 'could not save data'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})

            return HttpResponse(json.dumps(response), content_type="application/json")
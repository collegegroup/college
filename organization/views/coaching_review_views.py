from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from ..jsonparser.coaching_review_json import CoachingReviewJsonParser
from ..coaching_review_services import CoachingReviewORM
import json
__author__ = 'ravi'


class AddCoachingReview(APIView):

    def post(self, request):
        if request.method == "POST":
            response = dict()
            try:
                coaching_review_helper = CoachingReviewJsonParser.coaching_review_json_parser(request.POST.
                                                                                              get('jsonData'))
                CoachingReviewORM.save_coaching_review(coaching_review_helper)
                response.update({'message': "date saved successfully"})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                print ("error is ", ex)
                response.update({'message': 'could not save data'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})

            return HttpResponse(json.dumps(response), content_type="application/json")
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
import json


class CollegeReview(APIView):

    def post(self, request):
        if request.method == "POST":
            response = dict()
            try:
                # data = CollegeReviewJsonParser.college_review_json_parser(request.POST.get('jsonData'))
                response.update({'data': ""})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                print ("error is ", ex)
                response.update({'message': 'could not save data'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})

            return HttpResponse(json.dumps(response), content_type="application/json")